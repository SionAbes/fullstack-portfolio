from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://test:var_postgres_password@db:5432/test"

Session = scoped_session(sessionmaker())
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
Session.configure(bind=engine)
