from pydantic import BaseModel

class IntrstPayBase(BaseModel):
    IntrstPayUs234A: int
    IntrstPayUs234B: int
    IntrstPayUs234C: int
    LateFilingFee234F: int

class IntrstPayCreate(IntrstPayBase):
    pass

class IntrstPayUpdate(IntrstPayBase):
    pass

class IntrstPay(IntrstPayBase):
    id: int
    itr1_tax_computation_id: int

    class Config:
        orm_mode = True


class ITR1TaxComputationBase(BaseModel):
    TotalTaxPayable: int
    Rebate87A: int
    TaxPayableOnRebate: int
    EducationCess: int
    GrossTaxLiability: int
    Section89: int
    NetTaxLiability: int
    TotalIntrstPay: int
    TotTaxPlusIntrstPay: int
    IntrstPay: IntrstPay

class ITR1TaxComputationCreate(ITR1TaxComputationBase):
    pass

class ITR1TaxComputationUpdate(ITR1TaxComputationBase):
    pass

class ITR1TaxComputation(ITR1TaxComputationBase):
    id: int

    class Config:
        orm_mode = True


##+++++++++++++++++++++++++++++++++++Tax Paid======================================##
class TaxesPaidBase(BaseModel):
    AdvanceTax: int
    TDS: int
    TCS: int
    SelfAssessmentTax: int
    TotalTaxesPaid: int

class TaxesPaidCreate(TaxesPaidBase):
    pass

class TaxesPaidUpdate(TaxesPaidBase):
    pass

class TaxesPaid(TaxesPaidBase):
    id: int

    class Config:
        orm_mode = True
