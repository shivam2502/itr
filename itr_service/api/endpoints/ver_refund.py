from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import get_db

# Import the necessary models and schemas
from database.sections.verification import Verification as vdb, Declaration as ddb
from database.schemas.ver_refund import (
    DeclarationCreate,
    DeclarationUpdate,
    RefundCreate,
    RefundUpdate,
    VerificationCreate,
    VerificationUpdate,
    Declaration,
    Verification,
    Refund,
    BankAccountDtls,
    BankAccountDtlsCreate,
    BankAccountDtlsUpdate,
)

# Import the get_db function to get the database session
from database.db_config import get_db

# Create the API router
verdec_router = APIRouter()


# Define CRUD endpoints for Verification
@verdec_router.post("/verification/", response_model=Verification)
def create_verification(verification: VerificationCreate, db: Session = Depends(get_db)):
    db_verification = vdb(**verification.dict())
    db.add(db_verification)
    db.commit()
    db.refresh(db_verification)
    return db_verification

@verdec_router.get("/verification/{verification_id}", response_model=Verification)
def read_verification(verification_id: int, db: Session = Depends(get_db)):
    db_verification = db.query(vdb).filter(vdb.id == verification_id).first()
    if db_verification is None:
        raise HTTPException(status_code=404, detail="Verification not found")
    return db_verification

# Similar endpoints for update and delete can be defined here.


# Define CRUD endpoints for Declaration
@verdec_router.post("/declaration/", response_model=Declaration)
def create_declaration(declaration: DeclarationCreate, db: Session = Depends(get_db)):
    db_declaration = ddb(**declaration.dict())
    db.add(db_declaration)
    db.commit()
    db.refresh(db_declaration)
    return db_declaration

@verdec_router.get("/declaration/{declaration_id}", response_model=Declaration)
def read_declaration(declaration_id: int, db: Session = Depends(get_db)):
    db_declaration = db.query(ddb).filter(ddb.id == declaration_id).first()
    if db_declaration is None:
        raise HTTPException(status_code=404, detail="Declaration not found")
    return db_declaration

# Similar endpoints for update and delete can be defined here.


# Define CRUD endpoints for Refund
@verdec_router.post("/refund/", response_model=Refund)
def create_refund(refund: RefundCreate, db: Session = Depends(get_db)):
    db_refund = Refund(**refund.dict())
    db.add(db_refund)
    db.commit()
    db.refresh(db_refund)
    return db_refund

@verdec_router.get("/refund/{refund_id}", response_model=Refund)
def read_refund(refund_id: int, db: Session = Depends(get_db)):
    db_refund = db.query(Refund).filter(Refund.id == refund_id).first()
    if db_refund is None:
        raise HTTPException(status_code=404, detail="Refund not found")
    return db_refund

# Similar endpoints for update and delete can be defined here.
