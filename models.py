from sqlalchemy import Column, Integer, String
from db import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
