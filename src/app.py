from fastapi import FastAPI

from src.routes import rpn_router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(rpn_router, prefix="/rpn", tags=["rpn"])

    return app