from datetime import datetime
from app import db
# from flask_sqlalchemy.model import DefaultMeta
# BaseModel: DefaultMeta = db.Model
from sqlalchemy.ext.declarative import DeclarativeMeta # type: ignore

BaseModel: DeclarativeMeta = db.Model


class Todo(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id
