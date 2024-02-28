from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.databes import BASE


class User(BASE):
  __tablename__ = "users"
  
  users_ID = Column(Integer, primary_key=True, index=True)
  users_name = Column(String, index=True, nullable=False)
  users_password = Column(String, nullable=False, index=True)
  abone_id = Column(Integer, index=True, ForeignKey = "abone.abone_ID")
  plate_id = Column(Integer, index= True, ForeignKey = "plate.plate_ID")
  
  abone = relationship("Abone", back_populates="abone_id")
  plate = relationship("Plate", back_populates="plate_id" )