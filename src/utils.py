from dateutil.relativedelta import relativedelta
from datetime import date
from src.models.models_pydantic import UserCreatePayload
from src.models.models_sqlalchemy import Users
from src.db.database import db_engine, SessionLocal
from src.models import models_sqlalchemy


def db_session_generator():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_session():
    return next(db_session_generator())

def create_db():
    models_sqlalchemy.Base.metadata.create_all(bind=db_engine)

def get_age_from_dob(dob: date) -> int:
    today = date.today()
    age = relativedelta(today, dob)
    return age.years

def create_user(payload: UserCreatePayload):
    db = get_db_session()
    new_user = Users(**payload.model_dump())
    new_user.age = get_age_from_dob(new_user.dob)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users():
    db = get_db_session()
    users = db.query(Users).all()
    return users

def delete_user(user_id):
    db = get_db_session()
    user = db.query(Users).filter(Users.id == user_id).first()
    db.delete(user)
    db.commit()
