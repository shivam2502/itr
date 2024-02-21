from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

def creat_app() -> FastAPI:
    app = FastAPI(
        title=os.getenv("TITLE"),
        version=os.getenv("VERSION"),
        description=os.getenv("DESC")
    )
    return app

app = creat_app()


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
