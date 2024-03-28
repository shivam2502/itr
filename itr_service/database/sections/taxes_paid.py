from database.common_imports import *


class TaxesPaid(Base):
    __tablename__ = 'taxes_paid'

    id = Column(Integer, primary_key=True)
    AdvanceTax = Column(Integer)
    TDS = Column(Integer)
    TCS = Column(Integer)
    SelfAssessmentTax = Column(Integer)
    TotalTaxesPaid = Column(Integer)
