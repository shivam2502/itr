from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from api.endpoints import pi_api, tds, tax, ver_refund, inc_ded

routers = [pi_api.pi_router, tds.tds_router, tax.tax_router, ver_refund.verdec_router, inc_ded.id_router]

load_dotenv()

def creat_app() -> FastAPI:
    app = FastAPI(
        title="itr",
        version="0.0.1",
        description="itr page"
    )
    return app

app = creat_app()

[app.include_router(router) for router in routers]

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
