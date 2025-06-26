from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


db: SQLAlchemy = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = 'account'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    name: Mapped[str] = mapped_column(String(250), nullable=True)
    surname: Mapped[str] = mapped_column(String(250), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    weight: Mapped[int] = mapped_column(Integer, nullable=True)
    height: Mapped[int] = mapped_column(Integer, nullable=True)

class UserGoals(db.Model):
    __tablename__ = 'user_goals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    calory_intake: Mapped[int] = mapped_column(Integer, nullable=True)
    protein_intake: Mapped[int] = mapped_column(Integer, nullable=True)
    carbs_intake: Mapped[int] = mapped_column(Integer, nullable=True)
    fat_intake: Mapped[int] = mapped_column(Integer, nullable=True)
    weight: Mapped[int] = mapped_column(Integer, nullable=True)

def Meal(db.Model):
    __tablename__ = 'meal'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=True)
    food_weight: Mapped[int] = mapped_column(Integer, nullable=True)
    calories: Mapped[int] = mapped_column(Integer, nullable=True)
    protein: Mapped[int] = mapped_column(Integer, nullable=True)
    carbs: Mapped[int] = mapped_column(Integer, nullable=True)
    fat: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
