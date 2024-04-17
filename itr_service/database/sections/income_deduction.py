from app.itr_service.database.common_imports import *

class ITR1IncomeDeductions(Base):
    __tablename__ = 'itr1_income_deductions'

    id = Column(Integer, primary_key=True)
    GrossSalary = Column(Integer)
    Salary = Column(Integer)
    PerquisitesValue = Column(Integer)
    ProfitsInSalary = Column(Integer)
    Increliefus89A = Column(Integer)
    Increliefus89AOS = Column(Integer)
    # Assuming the structure of IncomeNotified89AType is complex, so we'll serialize it separately
    IncomeNotified89A = Column(Integer)
    IncomeNotifiedOther89A = Column(Integer)
    NetSalary = Column(Integer)
    DeductionUs16 = Column(Integer)
    DeductionUs16ia = Column(Integer)
    EntertainmentAlw16ii = Column(Integer)
    ProfessionalTaxUs16iii = Column(Integer)
    IncomeFromSal = Column(Integer)
    TypeOfHP = Column(String)
    GrossRentReceived = Column(Integer)
    TaxPaidlocalAuth = Column(Integer)
    AnnualValue = Column(Integer)
    StandardDeduction = Column(Integer)
    InterestPayable = Column(Integer)
    ArrearsUnrealizedRentRcvd = Column(Integer)
    TotalIncomeOfHP = Column(Integer)
    IncomeOthSrc = Column(Integer)
    DeductionUs57iia = Column(Integer)
    GrossTotIncome = Column(Integer)
    TotalIncome = Column(Integer)

    # Relationship with nested models
    UsrDeductUndChapVIA = relationship("UsrDeductUndChapVIA", uselist=False)
    DeductUndChapVIA = relationship("DeductUndChapVIA", uselist=False)
    ExemptIncAgriOthUs10 = relationship("ExemptIncAgriOthUs10", uselist=False)


class UsrDeductUndChapVIA(Base):
    __tablename__ = 'usr_deduct_und_chap_via'

    id = Column(Integer, primary_key=True)
    Section80C = Column(Integer)
    Section80CCC = Column(Integer)
    Section80CCDEmployeeOrSE = Column(Integer)
    Section80CCD1B = Column(Integer)
    Section80CCDEmployer = Column(Integer)
    Section80D = Column(Integer)
    Section80DD = Column(Integer)
    Section80DDB = Column(Integer)
    Section80E = Column(Integer)
    Section80EE = Column(Integer)
    Section80EEA = Column(Integer)
    Section80EEB = Column(Integer)
    Section80G = Column(Integer)
    Section80GG = Column(Integer)
    Section80GGA = Column(Integer)
    Section80GGC = Column(Integer)
    AnyOthSec80CCH = Column(Integer)
    Section80U = Column(Integer)
    Section80TTA = Column(Integer)
    Section80TTB = Column(Integer)
    TotalChapVIADeductions = Column(Integer)

    # Foreign key to parent table
    itr1_income_deductions_id = Column(Integer, ForeignKey('itr1_income_deductions.id'))


class DeductUndChapVIA(Base):
    __tablename__ = 'deduct_und_chap_via'

    id = Column(Integer, primary_key=True)
    Section80C = Column(Integer)
    Section80CCC = Column(Integer)
    Section80CCDEmployeeOrSE = Column(Integer)
    Section80CCD1B = Column(Integer)
    Section80CCDEmployer = Column(Integer)
    Section80D = Column(Integer)
    Section80DD = Column(Integer)
    Section80DDB = Column(Integer)
    Section80E = Column(Integer)
    Section80EE = Column(Integer)
    Section80EEA = Column(Integer)
    Section80EEB = Column(Integer)
    Section80G = Column(Integer)
    Section80GG = Column(Integer)
    Section80GGA = Column(Integer)
    Section80GGC = Column(Integer)
    AnyOthSec80CCH = Column(Integer)
    Section80U = Column(Integer)
    Section80TTA = Column(Integer)
    Section80TTB = Column(Integer)
    TotalChapVIADeductions = Column(Integer)

    # Foreign key to parent table
    itr1_income_deductions_id = Column(Integer, ForeignKey('itr1_income_deductions.id'))


class ExemptIncAgriOthUs10(Base):
    __tablename__ = 'exempt_inc_agri_oth_us10'

    id = Column(Integer, primary_key=True)
    ExemptIncAgriOthUs10Total = Column(Integer)

    # Relationship with nested model
    ExemptIncAgriOthUs10Dtls = relationship("ExemptIncAgriOthUs10Dtls")


class ExemptIncAgriOthUs10Dtls(Base):
    __tablename__ = 'exempt_inc_agri_oth_us10_dtls'

    id = Column(Integer, primary_key=True)
    NatureDesc = Column(String)
    OthAmount = Column(Integer)

    # Foreign key to parent table
    exempt_inc_agri_oth_us10_id = Column(Integer, ForeignKey('exempt_inc_agri_oth_us10.id'))
