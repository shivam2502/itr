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

if __name__ == "__main__":
    print(os.getenv("TITLE"))
    app = creat_app()
    uvicorn.run(app, host=os.getenv("HOST"), port=os.getenv("PORT"))
