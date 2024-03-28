from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db


# Import the necessary models and schemas
from database.sections.tds_otherthan_sal import TDSonOthThanSals as tds_db
from database.sections.tds_salary import TDSonSalaries as tds_sal_db
from database.schemas.tds import (
    EmployerOrDeductorOrCollectDetlCreate,
    EmployerOrDeductorOrCollectDetlUpdate,
    TDSonOthThanSalsCreate,
    TDSonOthThanSalsUpdate,
    TDSonOthThanSals as TDSonOthThanSalsSchema,
    TDSonSalariesCreate,
    TDSonSalariesUpdate,
    TDSonSalaries as TDSonSalariesSchema,
)

# Import the get_db function to get the database session
from database import get_db

# Create the API router
tds_router = APIRouter()


# Define CRUD endpoints for TDSonSalaries
@tds_router.post("/tds_salaries/", response_model=TDSonSalariesSchema)
def create_tds_salaries(tds_salaries: TDSonSalariesCreate, db: Session = Depends(get_db)):
    db_tds_salaries = tds_sal_db(**tds_salaries.dict())
    db.add(db_tds_salaries)
    db.commit()
    db.refresh(db_tds_salaries)
    return db_tds_salaries

@tds_router.get("/tds_salaries/{tds_salaries_id}", response_model=TDSonSalariesSchema)
def read_tds_salaries(tds_salaries_id: int, db: Session = Depends(get_db)):
    db_tds_salaries = db.query(tds_sal_db).filter(tds_sal_db.id == tds_salaries_id).first()
    if db_tds_salaries is None:
        raise HTTPException(status_code=404, detail="TDS on salaries not found")
    return db_tds_salaries

# Similar endpoints for update and delete can be defined here.


# Define CRUD endpoints for TDSonOthThanSals
@tds_router.post("/tds_oth_than_sal/", response_model=TDSonOthThanSalsSchema)
def create_tds_oth_than_sals(tds_oth_than_sals: TDSonOthThanSalsCreate, db: Session = Depends(get_db)):
    db_tds_oth_than_sals = tds_db(**tds_oth_than_sals.dict())
    db.add(db_tds_oth_than_sals)
    db.commit()
    db.refresh(db_tds_oth_than_sals)
    return db_tds_oth_than_sals

@tds_router.get("/tds_oth_than_sal/{tds_oth_than_sals_id}", response_model=TDSonOthThanSalsSchema)
def read_tds_oth_than_sals(tds_oth_than_sals_id: int, db: Session = Depends(get_db)):
    db_tds_oth_than_sals = db.query(tds_db).filter(tds_db.id == tds_oth_than_sals_id).first()
    if db_tds_oth_than_sals is None:
        raise HTTPException(status_code=404, detail="TDS on other than salaries not found")
    return db_tds_oth_than_sals

# Similar endpoints for update and delete can be defined here.
