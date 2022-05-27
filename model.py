from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import get_config

db = SQLAlchemy()
config = dict()
config = get_config()
migrate = Migrate()


class FyyurSession():
    def add(self) -> None:
        db.session.add(self)

    def delete(self) -> None:
        db.session.delete(self)

    def flush(self) -> None:
        db.session.flush()

    def commit(self) -> None:
        db.session.commit()

    def refresh(self) -> None:
        db.session.refresh(self)

    def rollback(self) -> None:
        db.session.rollback()

    def close(self) -> None:
        db.session.close()

class Student(db.Model, FyyurSession):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

    def format(self) -> dict:
        return {'id': self.id, 'name': self.name}

    def __repr__(self) -> str:
        return f'{self.id} - {self.name}'