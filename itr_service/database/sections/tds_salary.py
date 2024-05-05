from database.common_imports import *

class EmployerOrDeductorOrCollectDetl(Base):
    __tablename__ = 'employer_or_deductor_or_collect_detl'

    id = Column(Integer, primary_key=True)
    TAN = Column(String)
    EmployerOrDeductorOrCollecterName = Column(String)


class TDSonSalary(Base):
    __tablename__ = 'tds_on_salary'

    id = Column(Integer, primary_key=True)
    IncChrgSal = Column(Integer)
    TotalTDSSal = Column(Integer)

    # Relationship with nested model
    employer_or_deductor_or_collect_detl_id = Column(Integer, ForeignKey('employer_or_deductor_or_collect_detl.id'))
    EmployerOrDeductorOrCollectDetl = relationship("EmployerOrDeductorOrCollectDetl", uselist=False)


class TDSonSalaries(Base):
    __tablename__ = 'tds_on_salaries'

    id = Column(Integer, primary_key=True)
    TotalTDSonSalaries = Column(Integer)

    # Relationship with nested model
    TDSonSalary = relationship("TDSonSalary", cascade="all, delete-orphan")
