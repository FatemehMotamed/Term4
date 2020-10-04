
from sqlalchemy import create_engine, Column, String, Table, Integer, MetaData

engine = create_engine("mysql+pymysql://poulstar:poulstar@localhost/my_db")

engine.connect()

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String(100)),
   Column('lastname', String(100)),
)
meta.create_all(engine)