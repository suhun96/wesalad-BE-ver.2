from sqlalchemy     import Boolean, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import *
from database.settings       import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    name2 = Column(String(120), nullable=False)