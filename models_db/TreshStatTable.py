from sqlalchemy import Column, Integer, DateTime, String
from database import Base
import pytz 
from datetime import datetime


def get_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))

class TrashStatTable(Base):
    __tablename__ = "trash_stat_table"

    id = Column(Integer, primary_key=True)
    id_object = Column(String, nullable=False)
    date_detection = Column(DateTime, nullable=False, default=get_time)

