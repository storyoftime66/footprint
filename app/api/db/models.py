from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_path = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    photographer = Column(String)
    taken_time = Column(DateTime)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, default=datetime.now())
