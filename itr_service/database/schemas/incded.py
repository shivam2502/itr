from pydantic import BaseModel
from typing import List, Optional

class ExemptIncAgriOthUs10DtlsBase(BaseModel):
    NatureDesc: str
    OthAmount: int

class ExemptIncAgriOthUs10DtlsCreate(ExemptIncAgriOthUs10DtlsBase):
    pass

class ExemptIncAgriOthUs10DtlsUpdate(ExemptIncAgriOthUs10DtlsBase):
    pass

class ExemptIncAgriOthUs10Dtls(ExemptIncAgriOthUs10DtlsBase):
    id: int

    class Config:
        orm_mode = True


class ExemptIncAgriOthUs10Base(BaseModel):
    ExemptIncAgriOthUs10Total: int

class ExemptIncAgriOthUs10Create(ExemptIncAgriOthUs10Base):
    pass

class ExemptIncAgriOthUs10Update(ExemptIncAgriOthUs10Base):
    pass

class ExemptIncAgriOthUs10(ExemptIncAgriOthUs10Base):
    id: int
    exempt_inc_agri_oth_us10_dtls: List[ExemptIncAgriOthUs10Dtls]

    class Config:
        orm_mode = True


class DeductUndChapVIABase(BaseModel):
    Section80C: int
    Section80CCC: int
    Section80CCDEmployeeOrSE: int
    Section80CCD1B: int
    Section80CCDEmployer: int
    Section80D: int
    Section80DD: int
    Section80DDB: int
    Section80E: int
    Section80EE: int
    Section80EEA: int
    Section80EEB: int
    Section80G: int
    Section80GG: int
    Section80GGA: int
    Section80GGC: int
    AnyOthSec80CCH: int
    Section80U: int
    Section80TTA: int
    Section80TTB: int
    TotalChapVIADeductions: int

class DeductUndChapVIACreate(DeductUndChapVIABase):
    pass

class DeductUndChapVIAUpdate(DeductUndChapVIABase):
    pass

class DeductUndChapVIA(DeductUndChapVIABase):
    id: int

    class Config:
        orm_mode = True


class UsrDeductUndChapVIABase(BaseModel):
    Section80C: int
    Section80CCC: int
    Section80CCDEmployeeOrSE: int
    Section80CCD1B: int
    Section80CCDEmployer: int
    Section80D: int
    Section80DD: int
    Section80DDB: int
    Section80E: int
    Section80EE: int
    Section80EEA: int
    Section80EEB: int
    Section80G: int
    Section80GG: int
    Section80GGA: int
    Section80GGC: int
    AnyOthSec80CCH: int
    Section80U: int
    Section80TTA: int
    Section80TTB: int
    TotalChapVIADeductions: int

class UsrDeductUndChapVIACreate(UsrDeductUndChapVIABase):
    pass

class UsrDeductUndChapVIAUpdate(UsrDeductUndChapVIABase):
    pass

class UsrDeductUndChapVIA(UsrDeductUndChapVIABase):
    id: int

    class Config:
        orm_mode = True


class ITR1IncomeDeductionsBase(BaseModel):
    GrossSalary: int
    Salary: int
    PerquisitesValue: int
    ProfitsInSalary: int
    Increliefus89A: int
    Increliefus89AOS: int
    IncomeNotified89A: int
    IncomeNotifiedOther89A: int
    NetSalary: int
    DeductionUs16: int
    DeductionUs16ia: int
    EntertainmentAlw16ii: int
    ProfessionalTaxUs16iii: int
    IncomeFromSal: int
    TypeOfHP: Optional[str]
    GrossRentReceived: int
    TaxPaidlocalAuth: int
    AnnualValue: int
    StandardDeduction: int
    InterestPayable: int
    ArrearsUnrealizedRentRcvd: int
    TotalIncomeOfHP: int
    IncomeOthSrc: int
    DeductionUs57iia: int
    GrossTotIncome: int
    TotalIncome: int

class ITR1IncomeDeductionsCreate(ITR1IncomeDeductionsBase):
    pass

class ITR1IncomeDeductionsUpdate(ITR1IncomeDeductionsBase):
    pass

class ITR1IncomeDeductions(ITR1IncomeDeductionsBase):
    id: int
    usr_deduct_und_chap_via: UsrDeductUndChapVIA
    deduct_und_chap_via: DeductUndChapVIA
    exempt_inc_agri_oth_us10: ExemptIncAgriOthUs10

    class Config:
        orm_mode = True
