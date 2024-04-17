from app.itr_service.database.common_imports import *

class PersonalInfo(Base):
    __tablename__ = 'personal_info'

    id = Column(Integer, primary_key=True)
    assessee_name_id = Column(Integer, ForeignKey('assessee_name.id'))
    pan = Column(String(10), unique=True)
    address_id = Column(Integer, ForeignKey('address.id'))
    dob = Column(String)
    employer_category = Column(Enum('OTH', 'GOV', 'PSU'))
    aadhaar_card_no = Column(String)

    assessee_name = relationship("AssesseeName")
    address = relationship("Address")

class AssesseeName(Base):
    __tablename__ = 'assessee_name'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    sur_name_or_org_name = Column(String)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    residence_no = Column(String)
    residence_name = Column(String)
    road_or_street = Column(String)
    locality_or_area = Column(String)
    city_or_town_or_district = Column(String)
    state_code = Column(String)
    country_code = Column(String)
    pin_code = Column(Integer)
    country_code_mobile = Column(Integer)
    mobile_no = Column(Integer)
    email_address = Column(EmailType)


