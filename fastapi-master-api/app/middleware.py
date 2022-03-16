from app.settings import Settings
from fastapi import Request


async def db_session_middleware(request: Request, call_next, settings: Settings):
    Session = request.app.state.Session
    session = Session()
    request.state.db = session

    try:
        response = await call_next(request)

        # This setting is meant to enable us replacing this with transactional tests. See
        # conftest.py
        if settings.SKIP_SESSION_HANDLER:
            return response

        session.commit()
        session.close()

        return response
    except Exception as error:
        session.rollback()
        session.close()
        raise error
    finally:
        request.state.db = None
