from app.itr_service.database.common_imports import *

class Verification(Base):
    __tablename__ = 'verification'

    id = Column(Integer, primary_key=True)
    Declaration_AssesseeVerName = Column(String)
    Declaration_FatherName = Column(String)
    Declaration_AssesseeVerPAN = Column(String)
    Capacity = Column(Enum("S", "O", name="capacity_enum"))
    Place = Column(String)


class Declaration(Base):
    __tablename__ = 'declaration'

    id = Column(Integer, primary_key=True)
    AssesseeVerName = Column(String)
    FatherName = Column(String)
    AssesseeVerPAN = Column(String)

    # Relationship with parent table
    verification_id = Column(Integer, ForeignKey('verification.id'))


class CapacityEnum(str, Enum):
    S = "S"
    O = "O"
