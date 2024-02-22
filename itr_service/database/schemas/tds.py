from pydantic import BaseModel
from typing import List, Optional

class EmployerOrDeductorOrCollectDetlBase(BaseModel):
    TAN: str
    EmployerOrDeductorOrCollecterName: str

class EmployerOrDeductorOrCollectDetlCreate(EmployerOrDeductorOrCollectDetlBase):
    pass

class EmployerOrDeductorOrCollectDetlUpdate(EmployerOrDeductorOrCollectDetlBase):
    pass

class EmployerOrDeductorOrCollectDetl(EmployerOrDeductorOrCollectDetlBase):
    id: int

    class Config:
        orm_mode = True

class TDSonSalaryBase(BaseModel):
    IncChrgSal: int
    TotalTDSSal: int

class TDSonSalaryCreate(TDSonSalaryBase):
    pass

class TDSonSalaryUpdate(TDSonSalaryBase):
    pass

class TDSonSalary(TDSonSalaryBase):
    id: int
    employer_or_deductor_or_collect_detl_id: int

    class Config:
        orm_mode = True

class TDSonSalariesBase(BaseModel):
    TotalTDSonSalaries: int

class TDSonSalariesCreate(TDSonSalariesBase):
    pass

class TDSonSalariesUpdate(TDSonSalariesBase):
    pass

class TDSonSalaries(TDSonSalariesBase):
    id: int
    tds_on_salary: List[TDSonSalary]

    class Config:
        orm_mode = True


##++++++++++++++++++++++++++++++++++++TdsOnOtherThanSalary===========================##
    

class TDSonOthThanSalBase(BaseModel):
    AmtForTaxDeduct: int
    DeductedYr: str
    TotTDSOnAmtPaid: int
    ClaimOutOfTotTDSOnAmtPaid: int

class TDSonOthThanSalCreate(TDSonOthThanSalBase):
    pass

class TDSonOthThanSalUpdate(TDSonOthThanSalBase):
    pass

class TDSonOthThanSal(TDSonOthThanSalBase):
    id: int
    employer_or_deductor_or_collect_detl_id: int

    class Config:
        orm_mode = True

class TDSonOthThanSalsBase(BaseModel):
    TotalTDSonOthThanSals: int

class TDSonOthThanSalsCreate(TDSonOthThanSalsBase):
    pass

class TDSonOthThanSalsUpdate(TDSonOthThanSalsBase):
    pass

class TDSonOthThanSals(TDSonOthThanSalsBase):
    id: int
    tds_on_oth_than_sal: List[TDSonOthThanSal]

    class Config:
        orm_mode = True