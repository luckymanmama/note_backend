import uvicorn
from fastapi import FastAPI
from app.api.v1.router import api_router as api_v1_router
from app.api.core.config import settings


def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        debug=settings.APP_DEBUG,
        docs_url=settings.API_DOCS_URL,
    )
    app.include_router(api_v1_router, prefix=settings.API_V1_URL)
    return app


fastapi_app = get_application()

if __name__ == "__main__":
    uvicorn.run(
        fastapi_app,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
