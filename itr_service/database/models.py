from typing import List, Optional
from pydantic import BaseModel

class CreationInfo(BaseModel):
    SWVersionNo: str
    SWCreatedBy: str
    JSONCreatedBy: str
    JSONCreationDate: str
    IntermediaryCity: str
    Digest: str

class FormITR1(BaseModel):
    FormName: str
    Description: str
    AssessmentYear: str
    SchemaVer: str
    FormVer: str

class AssesseeName(BaseModel):
    FirstName: str
    MiddleName: str
    SurNameOrOrgName: str

class Address(BaseModel):
    ResidenceNo: str
    ResidenceName: str
    RoadOrStreet: str
    LocalityOrArea: str
    CityOrTownOrDistrict: str
    StateCode: str
    CountryCode: str
    PinCode: int
    CountryCodeMobile: int
    MobileNo: int
    EmailAddress: str

class PersonalInfo(BaseModel):
    AssesseeName: AssesseeName
    PAN: str
    Address: Address
    DOB: str
    EmployerCategory: str
    AadhaarCardNo: str

class FilingStatus(BaseModel):
    ReturnFileSec: int
    SeventhProvisio139: str
    NewTaxRegime: str
    clauseiv7provisio139i: str

class DateRange(BaseModel):
    Up16Of12To15Of3: int
    Up16Of3To31Of3: int
    Up16Of9To15Of12: int
    Upto15Of6: int
    Upto15Of9: int

class DividendInc(BaseModel):
    DateRange: DateRange

class OthersIncDtlsOthSrc(BaseModel):
    OthSrcNatureDesc: str
    OthSrcOthAmount: int
    DividendInc: Optional[DividendInc]

class OthersInc(BaseModel):
    OthersIncDtlsOthSrc: List[OthersIncDtlsOthSrc]

class UsrDeductUndChapVIA(BaseModel):
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

class DeductUndChapVIA(BaseModel):
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
    Section80U: int
    Section80TTA: int
    Section80TTB: int
    AnyOthSec80CCH: int
    TotalChapVIADeductions: int

class ExemptIncAgriOthUs10Dtls(BaseModel):
    NatureDesc: str
    OthAmount: int

class ExemptIncAgriOthUs10(BaseModel):
    ExemptIncAgriOthUs10Dtls: List[ExemptIncAgriOthUs10Dtls]
    ExemptIncAgriOthUs10Total: int

class ITR1IncomeDeductions(BaseModel):
    GrossSalary: int
    Salary: int
    PerquisitesValue: int
    ProfitsInSalary: int
    Increliefus89A: int
    Increliefus89AOS: int
    IncomeNotified89AType: List[dict]  # Define more specific model if possible
    IncomeNotified89A: int
    IncomeNotifiedOther89A: int
    NetSalary: int
    DeductionUs16: int
    DeductionUs16ia: int
    EntertainmentAlw16ii: int
    ProfessionalTaxUs16iii: int
    IncomeFromSal: int
    TypeOfHP: str
    GrossRentReceived: int
    TaxPaidlocalAuth: int
    AnnualValue: int
    StandardDeduction: int
    InterestPayable: int
    ArrearsUnrealizedRentRcvd: int
    TotalIncomeOfHP: int
    IncomeOthSrc: int
    OthersInc: OthersInc
    DeductionUs57iia: int
    GrossTotIncome: int
    UsrDeductUndChapVIA: UsrDeductUndChapVIA
    DeductUndChapVIA: DeductUndChapVIA
    TotalIncome: int
    ExemptIncAgriOthUs10: ExemptIncAgriOthUs10

class IntrstPay(BaseModel):
    IntrstPayUs234A: int
    IntrstPayUs234B: int
    IntrstPayUs234C: int
    LateFilingFee234F: int

class ITR1TaxComputation(BaseModel):
    TotalTaxPayable: int
    Rebate87A: int
    TaxPayableOnRebate: int
    EducationCess: int
    GrossTaxLiability: int
    Section89: int
    NetTaxLiability: int
    TotalIntrstPay: int
    IntrstPay: IntrstPay
    TotTaxPlusIntrstPay: int

class TaxesPaid(BaseModel):
    AdvanceTax: int
    TDS: int
    TCS: int
    SelfAssessmentTax: int
    TotalTaxesPaid: int

class BankAccountDtls(BaseModel):
    IFSCCode: str
    BankName: str
    BankAccountNo: str
    UseForRefund: str

class Refund(BaseModel):
    RefundDue: int
    BankAccountDtls: BankAccountDtls

class Declaration(BaseModel):
    AssesseeVerName: str
    FatherName: str
    AssesseeVerPAN: str

class Verification(BaseModel):
    Declaration: Declaration
    Capacity: str
    Place: str

class EmployerOrDeductorOrCollectDetl(BaseModel):
    TAN: str
    EmployerOrDeductorOrCollecterName: str

class TDSonSalary(BaseModel):
    EmployerOrDeductorOrCollectDetl: EmployerOrDeductorOrCollectDetl
    IncChrgSal: int
    TotalTDSSal: int

class TDSonSalaries(BaseModel):
    TDSonSalary: List[TDSonSalary]
    TotalTDSonSalaries: int

class TDSonOthThanSal(BaseModel):
    EmployerOrDeductorOrCollectDetl: EmployerOrDeductorOrCollectDetl
    AmtForTaxDeduct: int
    DeductedYr: str
    TotTDSOnAmtPaid: int
    ClaimOutOfTotTDSOnAmtPaid: int

class TDSonOthThanSals(BaseModel):
    TDSonOthThanSal: List[TDSonOthThanSal]
    TotalTDSonOthThanSals: int

class ITR1(BaseModel):
    CreationInfo: CreationInfo
    Form_ITR1: FormITR1
    PersonalInfo: PersonalInfo
    FilingStatus: FilingStatus
    ITR1_IncomeDeductions: ITR1IncomeDeductions
    ITR1_TaxComputation: ITR1TaxComputation
    TaxPaid: TaxesPaid
    Refund: Refund
    Verification: Verification
    TDSonSalaries: TDSonSalaries
    TDSonOthThanSals: TDSonOthThanSals
