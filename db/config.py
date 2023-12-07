import sqlalchemy
from sqlalchemy import select,update
from datetime import datetime
import pytz
from sqlalchemy import create_engine, BIGINT, TIMESTAMP, ForeignKey, VARCHAR, CheckConstraint, text, Column, func
from sqlalchemy.orm import declarative_base, Session, Mapped, mapped_column
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:1965@localhost:5432/lesson_6")
Base = declarative_base()
Session = Session(bind=engine)
uzbekistan_timezone = pytz.timezone('Asia/Tashkent')
current_time_in_uzbekistan = datetime.now(uzbekistan_timezone)


class User(Base):
    __tablename__ = "afitsant"
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, autoincrement=True, primary_key=True)
    fullname: Mapped[str] = mapped_column(__type_pos=VARCHAR,nullable=True)
    chat_id:Mapped[str]=mapped_column(nullable=True)

def get_all_users(session):
        query = select(User)
        result = session.execute(query)
        return result.fetchall()

Base.metadata.create_all(engine)

Ssession = sessionmaker(bind=engine)
session = Ssession()

def add_user(fulname, id):
    users = []
    for i in (get_all_users(session)):
        for j in i:
            users.append(j.fullname)
    if fulname not in users:
        new_user = User(fullname=fulname, chat_id=id,zakaz=n)
        session.add(new_user)
        session.commit()

