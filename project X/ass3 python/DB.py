from sqlalchemy import select
from connection import *
from crud import *
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy import create_engine



engine = db.create_engine('postgresql///ass3.db')

connection = engine.connect()

metadata = db.MetaData()

prodicts = db.Table('Products', metadata, 
                    db.Column('product_id', db.Integer, primary_key=True),
                    db.Column('product_name', db.Text),
                    db.Column('suplier_name', db.Text),
                    db.Column('price_per_tonne', db.Integer)
)

metadata.create_all(engine)



