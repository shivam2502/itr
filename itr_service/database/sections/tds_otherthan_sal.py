from common_imports import *

# EmployerOrDeductorOrCollectDetl class is imported from the previous code

class TDSonOthThanSal(Base):
    __tablename__ = 'tds_on_oth_than_sal'

    id = Column(Integer, primary_key=True)
    AmtForTaxDeduct = Column(Integer)
    DeductedYr = Column(String)
    TotTDSOnAmtPaid = Column(Integer)
    ClaimOutOfTotTDSOnAmtPaid = Column(Integer)

    # Relationship with nested model
    employer_or_deductor_or_collect_detl_id = Column(Integer, ForeignKey('employer_or_deductor_or_collect_detl.id'))
    EmployerOrDeductorOrCollectDetl = relationship("EmployerOrDeductorOrCollectDetl", uselist=False)


class TDSonOthThanSals(Base):
    __tablename__ = 'tds_on_oth_than_sals'

    id = Column(Integer, primary_key=True)
    TotalTDSonOthThanSals = Column(Integer)

    # Relationship with nested model
    TDSonOthThanSal = relationship("TDSonOthThanSal", cascade="all, delete-orphan")
