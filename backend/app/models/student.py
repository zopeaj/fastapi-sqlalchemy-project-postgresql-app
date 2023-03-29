from sqlalchemy import Integer, Column, String, Sequance
import sqlalchemy_utils
from app.db.base import Base

class Student(Base):
    id = Column(Integer, Sequance("student_id_seq"), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
