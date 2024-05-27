from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Замените строки ниже на свои параметры подключения
DATABASE_URI = 'postgresql://postgres:1488@localhost:5432/tresh_stat_db'

engine = create_engine(DATABASE_URI)

Base = declarative_base()
