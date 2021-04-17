from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql import Base

class Play(Base):
    __tablename__='play'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, default=True)
    caracter = Column(String, unique=True, index=True)
