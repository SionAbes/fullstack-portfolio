import functools
import io

import uvicorn
import yaml
from app.api.router import api_router
from app.settings import Settings, get_settings
from fastapi import FastAPI
from fastapi.responses import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_app(settings: Settings = None):
    app = FastAPI(
        title="Master Data API",
        version="1.0.0",
        docs_url="/",
    )
    settings = settings or get_settings()

    @app.get("/openapi.yaml", include_in_schema=False)
    @functools.lru_cache()
    def read_openapi_yaml() -> Response:
        openapi_json = app.openapi()
        yaml_s = io.StringIO()
        yaml.dump(openapi_json, yaml_s)
        return Response(yaml_s.getvalue(), media_type="text/yaml")

    app.include_router(api_router)

    # Database init
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
    session = sessionmaker(autocommit=False, bind=engine)
    app.state.session = session

    return app


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run("app.main:create_app", host="0.0.0.0", port=80, reload=True, debug=True)
