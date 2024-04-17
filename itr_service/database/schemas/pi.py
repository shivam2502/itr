from pydantic import BaseModel
from typing import Optional


class AssesseeNameSchema(BaseModel):
    id: int
    first_name: str
    middle_name: str
    sur_name_or_org_name: str

    class Config:
        orm_mode = True

class AddressSchema(BaseModel):
    id: int
    residence_no: str
    residence_name: str
    road_or_street: str
    locality_or_area: str
    city_or_town_or_district: str
    state_code: str
    country_code: str
    pin_code: int
    country_code_mobile: int
    mobile_no: int
    email_address: str

    class Config:
        orm_mode = True


class PersonalInfoSchema(BaseModel):
    id: int
    pan: str
    dob: str
    employer_category: str
    aadhaar_card_no: str
    assessee_name: Optional[AssesseeNameSchema]
    address: Optional[AddressSchema]

    class Config:
        orm_mode = True



class FilingStatusBase(BaseModel):
    ReturnFileSec: int
    SeventhProvisio139: str
    NewTaxRegime: str
    clauseiv7provisio139i: str