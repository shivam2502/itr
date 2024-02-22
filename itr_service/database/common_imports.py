from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from itr.itr_service.database.db_config import Base