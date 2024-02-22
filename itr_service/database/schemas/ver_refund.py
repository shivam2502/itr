from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VerificationBase(BaseModel):
    Declaration_AssesseeVerName: str
    Declaration_FatherName: str
    Declaration_AssesseeVerPAN: str
    Capacity: Optional[str]
    Place: Optional[str]

class VerificationCreate(VerificationBase):
    pass

class VerificationUpdate(VerificationBase):
    pass

class Verification(VerificationBase):
    id: int

    class Config:
        orm_mode = True


class DeclarationBase(BaseModel):
    AssesseeVerName: str
    FatherName: str
    AssesseeVerPAN: str

class DeclarationCreate(DeclarationBase):
    pass

class DeclarationUpdate(DeclarationBase):
    pass

class Declaration(DeclarationBase):
    id: int
    verification_id: int

    class Config:
        orm_mode = True


class CapacityEnum(str, Enum):
    S = "S"
    O = "O"


##===========================Refund========================================##
    

class BankAccountDtlsBase(BaseModel):
    IFSCCode: str
    BankName: str
    BankAccountNo: str
    UseForRefund: str

class BankAccountDtlsCreate(BankAccountDtlsBase):
    pass

class BankAccountDtlsUpdate(BankAccountDtlsBase):
    pass

class BankAccountDtls(BankAccountDtlsBase):
    id: int

    class Config:
        orm_mode = True


class RefundBase(BaseModel):
    RefundDue: int

class RefundCreate(RefundBase):
    pass

class RefundUpdate(RefundBase):
    pass

class Refund(RefundBase):
    id: int
    bank_account_dtls: BankAccountDtls

    class Config:
        orm_mode = True