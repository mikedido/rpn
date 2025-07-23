import uvicorn

from src.app import get_application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9010, reload=True)
