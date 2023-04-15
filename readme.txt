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

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USERNAME = "your-email@gmail.com"
SMTP_PASSWORD = "your-password"

# Function to send email
def send_email(subject: str, to_email: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        smtp_server = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp_server.sendmail(SMTP_USERNAME, to_email, msg.as_string())
        smtp_server.quit()
        return True
    except SMTPException:
        return False

# API endpoint to create user and send email
@app.post("/users/")
async def create_user(user_email: EmailStr, user_name: str, db: Session = Depends(get_db)):
    new_user = User(name=user_name, email=user_email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    subject = "Welcome to our app!"
    body = f"Hello {user_name},\n\nThank you for joining our app. We hope you enjoy using it.\n\nBest,\nOur Team"
    email_sent = send_email(subject, user_email, body)
    
    return {"user": new_user, "email_sent": email_sent}

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
