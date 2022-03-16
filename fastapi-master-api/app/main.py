import uvicorn
from app.api.router import api_router
from app.middleware import db_session_middleware
from app.settings import Settings, get_settings
from fastapi import FastAPI, Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_app(settings: Settings = None):
    app = FastAPI(
        title="Master Data API",
        version="1.0.0",
        docs_url="/",
    )
    settings = settings or get_settings()

    @app.middleware("http")
    async def session_handler(request: Request, call_next):
        return await db_session_middleware(request, call_next, settings)

    app.include_router(api_router)

    # Database init
    Session = sessionmaker(autocommit=False)
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
    Session.configure(bind=engine)

    app.state.Session = Session
    app.state.engine = engine

    return app


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run("app.main:create_app", host="0.0.0.0", port=80, reload=True, debug=True)
