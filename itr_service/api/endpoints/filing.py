from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import models, schemas
from database.db_config import get_db
# Create the APIRouter
router = APIRouter(prefix="/personal_info", tags=["PersonalInfo"])


class PersonalInfoAPI:
    @router.post("/", response_model=schemas.PersonalInfo)
    def create_personal_info(personal_info: schemas.PersonalInfoCreate, db: Session = Depends(get_db)):
        db_personal_info = models.PersonalInfo(**personal_info.dict())
        db.add(db_personal_info)
        db.commit()
        db.refresh(db_personal_info)
        return db_personal_info

    @router.get("/{personal_info_id}", response_model=schemas.PersonalInfo)
    def get_personal_info(personal_info_id: int, db: Session = Depends(get_db)):
        db_personal_info = db.query(models.PersonalInfo).filter(models.PersonalInfo.id == personal_info_id).first()
        if db_personal_info is None:
            raise HTTPException(status_code=404, detail="PersonalInfo not found")
        return db_personal_info


    @router.put("/{personal_info_id}", response_model=schemas.PersonalInfo)
    def update_personal_info(personal_info_id: int, personal_info: schemas.PersonalInfoUpdate, db: Session = Depends(get_db)):
        db_personal_info = db.query(models.PersonalInfo).filter(models.PersonalInfo.id == personal_info_id).first()
        if db_personal_info is None:
            raise HTTPException(status_code=404, detail="PersonalInfo not found")
        for key, value in personal_info.dict().items():
            setattr(db_personal_info, key, value)
        db.commit()
        db.refresh(db_personal_info)
        return db_personal_info


# Instantiate the class to create the API endpoints
personal_info_api = PersonalInfoAPI()
