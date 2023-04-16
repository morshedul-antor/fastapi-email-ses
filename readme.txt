### create database name 'todos'
### create '.env' file


******** run command *********
# python3 -m venv env
# source env/bin/activate
# pip3 install -r requirements.txt
# cd src
# alembic upgrade head
# python3 main.py 


*********** add the following lines into .env ************
DATABASE_URL=mysql+mysqlconnector://root:@localhost:3306/todos
URL_ONE=http://localhost:3000
URL_TWO=https://localhost:300


******** run command for authentication *********
# openssl rand -hex 32
# paste the key to SECRET_KEY


*********** add the following lines into .env ************
SECRET_KEY=d0edcf1fe0b762a3a3eaf06d49a396f175b29ce3ecd680c61e3a0f94292e206c
ALGORITHM=HS256
DATABASE_URL=mysql+mysqlconnector://root:@localhost:3306/todos
URL_ONE=http://localhost:3000
URL_TWO=https://localhost:300


##### Email Code #####
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import EmailStr
from smtplib import SMTPException, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Model definition
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))


