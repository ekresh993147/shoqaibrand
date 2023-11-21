from models import *
from sqlalchemy import create_engine

# connection to a sql server
def get_engine(conn_str="sqlite:///test.tb"):
    engine = create_engine(conn_str, echo=True, future=True)
    return engine

# Emit CREATE TABLE DDL
def create_table_ddl(engine):
    Base.metadata.create_all(engine)
