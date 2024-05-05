from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.sections import personal_info as pidb, filing_status as fsdb
from database.schemas import pi
from database.db_config import get_db
from typing import List

pi_router = APIRouter(prefix="/personal_info", tags=["PersonalInfo"])


@pi_router.post("/", response_model=pi.PersonalInfoSchema)
def create_personal_info(personal_info: pi.PersonalInfoSchema, db: Session = Depends(get_db)):
    db_personal_info = pidb.PersonalInfo(**personal_info)
    db.add(db_personal_info)
    db.commit()
    db.refresh(db_personal_info)
    return db_personal_info

@pi_router.get("/{personal_info_id}", response_model=pi.PersonalInfoSchema)
def get_personal_info(personal_info_id: int, db: Session = Depends(get_db)):
    db_personal_info = db.query(pidb.PersonalInfo).filter(pidb.PersonalInfo.id == personal_info_id).first()
    if db_personal_info is None:
        raise HTTPException(status_code=404, detail="PersonalInfo not found")
    return db_personal_info

@pi_router.get("/", response_model=List[pi.PersonalInfoSchema])
def get_personal_info_list(db: Session = Depends(get_db)):
    return db.query(pidb.PersonalInfo).all()

@pi_router.put("/{personal_info_id}", response_model=pi.PersonalInfoSchema)
def update_personal_info(personal_info_id: int, personal_info: pi.PersonalInfoSchema, 
                         db: Session = Depends(get_db)):
    db_personal_info = db.query(pidb.PersonalInfo).filter(pidb.PersonalInfo.id == personal_info_id).first()
    if db_personal_info is None:
        raise HTTPException(status_code=404, detail="PersonalInfo not found")
    for key, value in personal_info.dict().items():
        setattr(db_personal_info, key, value)
    db.commit()
    db.refresh(db_personal_info)
    return db_personal_info

@pi_router.delete("/{personal_info_id}", response_model=pi.PersonalInfoSchema)
def delete_personal_info(personal_info_id: int, db: Session = Depends(get_db)):
    db_personal_info = db.query(pidb.PersonalInfo).filter(pidb.PersonalInfo.id == personal_info_id).first()
    if db_personal_info is None:
        raise HTTPException(status_code=404, detail="PersonalInfo not found")
    db.delete(db_personal_info)
    db.commit()
    return db_personal_info



##====================================================================================
@pi_router.post("/", response_model=pi.FilingStatusBase)
def create_filing_status(filing_status: pi.FilingStatusBase, db: Session = Depends(get_db)):
    db_filing_status = fsdb.FilingStatus(**filing_status.dict())
    db.add(db_filing_status)
    db.commit()
    db.refresh(db_filing_status)
    return db_filing_status

@pi_router.get("/{filing_status_id}", response_model=pi.FilingStatusBase)
def read_filing_status(filing_status_id: int, db: Session = Depends(get_db)):
    db_filing_status = db.query(fsdb.FilingStatus).filter(fsdb.FilingStatus.id == filing_status_id).first()
    if db_filing_status is None:
        raise HTTPException(status_code=404, detail="Filing status not found")
    return db_filing_status

@pi_router.get("/", response_model=List[pi.FilingStatusBase])
def read_all_filing_status(db: Session = Depends(get_db)):
    return db.query(fsdb.FilingStatus).all()

@pi_router.put("/{filing_status_id}", response_model=pi.FilingStatusBase)
def update_filing_status(filing_status_id: int, filing_status: pi.FilingStatusBase, db: Session = Depends(get_db)):
    db_filing_status = db.query(fsdb.FilingStatus).filter(fsdb.FilingStatus.id == filing_status_id).first()
    if db_filing_status is None:
        raise HTTPException(status_code=404, detail="Filing status not found")
    for attr, value in filing_status.dict().items():
        setattr(db_filing_status, attr, value)
    db.commit()
    db.refresh(db_filing_status)
    return db_filing_status

@pi_router.delete("/{filing_status_id}", response_model=pi.FilingStatusBase)
def delete_filing_status(filing_status_id: int, db: Session = Depends(get_db)):
    db_filing_status = db.query(fsdb.FilingStatus).filter(fsdb.FilingStatus.id == filing_status_id).first()
    if db_filing_status is None:
        raise HTTPException(status_code=404, detail="Filing status not found")
    db.delete(db_filing_status)
    db.commit()
    return db_filing_status
