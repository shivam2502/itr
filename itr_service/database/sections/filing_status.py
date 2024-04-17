from app.itr_service.database.common_imports import *


class FilingStatus(Base):
    __tablename__ = 'filing_status'

    id = Column(Integer, primary_key=True)
    ReturnFileSec = Column(Integer)
    SeventhProvisio139 = Column(String)
    NewTaxRegime = Column(String)
    clauseiv7provisio139i = Column(String)