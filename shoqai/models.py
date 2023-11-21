from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

# Base class will apply the declarative mapping process to all subclasses
# Also describes real SQL tables that exist, or will exist
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True) # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    user_sname = Column(String(255))
    password = Column(String(255), nullable=False)

    # user_cars = relationship("Car", back_populates = "owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_sname!r})"