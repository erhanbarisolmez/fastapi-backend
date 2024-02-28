from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.databes import BASE


class Abone(BASE):
  __tablename__="abone"
  
  abone_ID = Column(Integer, primary_key=True, index=True)
  abone_name = Column(String, index=True, nullable=False)
  users_password = Column(String, nullable=False, index=True)
  
  user = relationship("User", back_populates="abone")