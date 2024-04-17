from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importing models and schemas
from app.itr_service.database.sections.income_deduction import ITR1IncomeDeductions
from app.itr_service.database.schemas.incded import (
    ITR1IncomeDeductionsCreate,
    ITR1IncomeDeductionsUpdate,
    ITR1IncomeDeductions,
)

# Importing database dependency
from app.itr_service.database.db_config import get_db

# Define router
id_router = APIRouter()


# Define dependency for retrieving income and deductions by ID
def read_income_deductions(income_deductions_id: int, db: Session = Depends(get_db)):
    db_income_deductions = db.query(ITR1IncomeDeductions).filter(ITR1IncomeDeductions.id == income_deductions_id).first()
    if db_income_deductions is None:
        raise HTTPException(status_code=404, detail="Income and deductions not found")
    return db_income_deductions


# API endpoint to read income and deductions by ID
@id_router.get("/income_deductions/{income_deductions_id}", response_model=ITR1IncomeDeductions)
def get_income_deductions(income_deductions_id: int, db: Session = Depends(get_db)):
    return read_income_deductions(income_deductions_id, db)


# API endpoint to create income and deductions
@id_router.post("/income_deductions/", response_model=ITR1IncomeDeductions)
def create_income_deductions(income_deductions: ITR1IncomeDeductionsCreate, db: Session = Depends(get_db)):
    db_income_deductions = ITR1IncomeDeductions(**income_deductions.dict())
    db.add(db_income_deductions)
    db.commit()
    db.refresh(db_income_deductions)
    return db_income_deductions


# API endpoint to update income and deductions by ID
@id_router.put("/income_deductions/{income_deductions_id}", response_model=ITR1IncomeDeductions)
def update_income_deductions(income_deductions_id: int, income_deductions: ITR1IncomeDeductionsUpdate, db: Session = Depends(get_db)):
    db_income_deductions = read_income_deductions(income_deductions_id, db)
    for key, value in income_deductions.dict().items():
        setattr(db_income_deductions, key, value)
    db.commit()
    db.refresh(db_income_deductions)
    return db_income_deductions
