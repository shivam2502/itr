from fastapi import FastAPI
# from itr_service.api.endpoints import filing
from core.config import settings
# from itr_service.core.database import create_db_and_tables

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

# Include routes from different endpoints
# app.include_router(authentication.router, prefix="/auth", tags=["Authentication"])
# app.include_router(filing.router, prefix="/filing", tags=["Filing"])
# app.include_router(user_data.router, prefix="/user", tags=["User Data"])

# Initialize database and create tables (if needed)
# create_db_and_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
