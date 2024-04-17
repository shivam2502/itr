from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

import sys

sys.path.append("api")

from app.itr_service.api.endpoints.inc_ded import id_router
from app.itr_service.api.endpoints.pi_api import pi_router
from app.itr_service.api.endpoints.tax import tax_router
from app.itr_service.api.endpoints.tds import tds_router
from app.itr_service.api.endpoints.ver_refund import verdec_router

load_dotenv()

def creat_app() -> FastAPI:
    app = FastAPI(
        title="ITR PAGE",
        version=0.1,
        description="Utility to explain ITR 1"
    )
    return app
app = creat_app()
app.include_router(pi_router, prefix="/personal_info", tags=["personal_info"])
app.include_router(id_router, prefix="/income_deduction", tags=["income_deduction"])
app.include_router(tax_router, prefix="/tax", tags=["tax"])
app.include_router(tds_router, prefix="/tds", tags=["tds"])
app.include_router(verdec_router, prefix="/verdec", tags=["verification_and_declaration"])


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
