from database.common_imports import *

class ITR1TaxComputation(Base):
    __tablename__ = 'itr1_tax_computation'

    id = Column(Integer, primary_key=True)
    TotalTaxPayable = Column(Integer)
    Rebate87A = Column(Integer)
    TaxPayableOnRebate = Column(Integer)
    EducationCess = Column(Integer)
    GrossTaxLiability = Column(Integer)
    Section89 = Column(Integer)
    NetTaxLiability = Column(Integer)
    TotalIntrstPay = Column(Integer)
    TotTaxPlusIntrstPay = Column(Integer)

    # Relationship with nested model
    IntrstPay = relationship("IntrstPay", uselist=False)


class IntrstPay(Base):
    __tablename__ = 'intrst_pay'

    id = Column(Integer, primary_key=True)
    IntrstPayUs234A = Column(Integer)
    IntrstPayUs234B = Column(Integer)
    IntrstPayUs234C = Column(Integer)
    LateFilingFee234F = Column(Integer)

    # Foreign key to parent table
    itr1_tax_computation_id = Column(Integer, ForeignKey('itr1_tax_computation.id'))