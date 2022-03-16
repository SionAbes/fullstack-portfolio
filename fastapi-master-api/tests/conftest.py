import pytest
from app.dependancies import get_db
from app.main import create_app
from app.repository.models.base import BaseModel as Base
from app.security import get_current_user
from app.settings import Settings, get_settings
from sqlalchemy import create_engine
from sqlalchemy.event import listens_for
from sqlalchemy_utils import create_database, database_exists, drop_database
from starlette.testclient import TestClient
from tests import Session
from tests.factories.token import TokenModelFactory
from tests.factories.user import UserFactory


def get_settings_override():
    return Settings(
        ENV="local",
        SQL_HOST="127.0.0.1",
        SQL_PORT=5432,
        POSTGRES_DB="test",
        POSTGRES_USER="test",
        POSTGRES_PASSWORD="var_postgres_password",
        API_URL="http://127.0.0.1:80",
        JWT_SECRET="jwt_secret",
        HASH_SECRET="6SzoYaa8bcAvS7-rGcUQV_xxZGQgwgHJNGo5xgfQGJ4=",
        ACCESS_TOKEN_EXPIRE_MINUTES=30,
        REFRESH_TOKEN_EXPIRE_MINUTES=60,
        ALGORITHM="HS256",
    )


@pytest.fixture(scope="function")
def app():
    app = create_app(settings=get_settings_override())
    app.dependency_overrides[get_settings] = get_settings_override
    return app


@pytest.fixture(scope="function")
def settings():
    return get_settings_override()


@pytest.fixture(scope="function")
def connection(settings):
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

    if database_exists(settings.SQLALCHEMY_DATABASE_URL):
        drop_database(settings.SQLALCHEMY_DATABASE_URL)

    create_database(settings.SQLALCHEMY_DATABASE_URL)

    connection = engine.connect()

    yield connection

    drop_database(settings.SQLALCHEMY_DATABASE_URL)
    connection.close()


@pytest.fixture(scope="function")
def setup_db(connection, request):
    """Setup test database.

    Creates all database tables as declared in SQLAlchemy schemas,
    then proceeds to drop all the created tables after all tests
    have finished running.
    """

    Base.metadata.create_all(bind=connection)

    return None


@pytest.fixture(autouse=True)
def session(app, connection, setup_db, request):
    transaction = connection.begin()
    session = Session(bind=connection)
    session.begin_nested()

    @listens_for(session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        """Support tests with rollbacks.

        This is required for tests that call some services that issue
        rollbacks in try-except blocks.

        With this event the Session always runs all operations within
        the scope of a SAVEPOINT, which is established at the start of
        each transaction, so that tests can also rollback the
        “transaction” as well while still remaining in the scope of a
        larger “transaction” that’s never committed.
        """
        if transaction.nested and not transaction._parent.nested:
            # ensure that state is expired the way session.commit() at
            # the top level normally does
            session.expire_all()
            session.begin_nested()

    def replace_application_session(*args, **kwargs):
        # This callable allows us to replace at runtime the
        # application's database session with the new test session,
        # which supports transactional tests.
        return session

    # This will depend on how you are declaring and handling the app's
    # database session. You will need to monkeypatch accordingly
    app.dependency_overrides[get_db] = lambda: session

    def teardown():
        Session.remove()
        transaction.rollback()

        Base.metadata.drop_all(bind=connection)

    request.addfinalizer(teardown)

    return session


@pytest.fixture(scope="function")
def client(app):
    with TestClient(app) as test_client:
        yield test_client


def login_as(app, token):
    app.dependency_overrides[get_current_user] = lambda: token


@pytest.fixture
def auth_user():
    return UserFactory(
        password="$2a$10$lSYipjr11mxzfeKDjYt6f.XA369N2SZsarMMRiFwoZ/PGS8.5ma7a",
        email="test_email",
    )


@pytest.fixture
def mock_admin_user(app, auth_user):
    admin_token = TokenModelFactory(sub=auth_user.id)
    login_as(app, admin_token)
    return admin_token


@pytest.fixture
def refresh_token(app, auth_user):
    refresh_token = TokenModelFactory(sub=auth_user.id, type="refresh_token")
    login_as(app, refresh_token)
    return refresh_token


@pytest.fixture
def mock_standard_user(app, auth_user):
    user_token = TokenModelFactory(sub=auth_user.id, roles=["USER"])
    login_as(app, user_token)
    return user_token
