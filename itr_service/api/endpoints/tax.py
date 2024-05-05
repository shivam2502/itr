from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Import the necessary models and schemas
from database.sections.tax_computation import ITR1TaxComputation as tax_db
from database.sections.taxes_paid import TaxesPaid
from database.schemas.taxc import (
    ITR1TaxComputationUpdate,
    ITR1TaxComputationCreate,
    TaxesPaidUpdate,
    TaxesPaidCreate,
    TaxesPaid as TaxesPaidSchema,
    ITR1TaxComputation as ITR1TaxComputationSchema,
    IntrstPay,
    IntrstPayCreate,
    IntrstPayUpdate,
)

# Import the get_db function to get the database session
from database.db_config import get_db

# Create the API router
tax_router = APIRouter()


# Define CRUD endpoints for ITR1TaxComputation
@tax_router.post("/tax_computation/", response_model=ITR1TaxComputationSchema)
def create_tax_computation(tax_computation: ITR1TaxComputationCreate, db: Session = Depends(get_db)):
    db_tax_computation = tax_db(**tax_computation.dict())
    db.add(db_tax_computation)
    db.commit()
    db.refresh(db_tax_computation)
    return db_tax_computation

@tax_router.get("/tax_computation/{tax_computation_id}", response_model=ITR1TaxComputationSchema)
def read_tax_computation(tax_computation_id: int, db: Session = Depends(get_db)):
    db_tax_computation = db.query(tax_db).filter(tax_db.id == tax_computation_id).first()
    if db_tax_computation is None:
        raise HTTPException(status_code=404, detail="Tax computation not found")
    return db_tax_computation

@tax_router.put("/tax_computation/{tax_computation_id}", response_model=ITR1TaxComputationSchema)
def update_tax_computation(tax_computation_id: int, tax_computation: ITR1TaxComputationUpdate, db: Session = Depends(get_db)):
    db_tax_computation = db.query(tax_db).filter(tax_db.id == tax_computation_id).first()
    if db_tax_computation is None:
        raise HTTPException(status_code=404, detail="Tax computation not found")
    for attr, value in tax_computation.dict().items():
        setattr(db_tax_computation, attr, value)
    db.commit()
    db.refresh(db_tax_computation)
    return db_tax_computation

@tax_router.delete("/tax_computation/{tax_computation_id}")
def delete_tax_computation(tax_computation_id: int, db: Session = Depends(get_db)):
    db_tax_computation = db.query(tax_db).filter(tax_db.id == tax_computation_id).first()
    if db_tax_computation is None:
        raise HTTPException(status_code=404, detail="Tax computation not found")
    db.delete(db_tax_computation)
    db.commit()
    return {"message": "Tax computation deleted successfully"}


# Similar CRUD endpoints for TaxesPaid and IntrstPay can be defined here.
