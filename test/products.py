from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#__tablename__  = 'sppres'

class Snaps(db.Model):
   __tablename__ = "snaps"
   id = db.Column(db.Integer, primary_key=True)
   version_id = db.Column(db.String(40), unique=True, nullable=False)
   date_added = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

   dp = db.relationship('DependentProduct', lazy='select', backref=db.backref('snaps', lazy='joined'))


   def __repr__(self):
      return '<Snaps %r>' % self.version_id


class DependentProduct(db.Model):
   __tablename__ = "dptable"
   id = db.Column(db.Integer, primary_key=True)
   version_id = db.Column(db.String(40), nullable=False)
   product_id = db.Column(db.String(40), nullable=False)
   version = db.Column(db.String(40), nullable=False)

   dp_id = db.Column(db.Integer, db.ForeignKey('snaps.id'),
        nullable=False)

   def __repr__(self):
      return '<DependentProduct %r>' % self.version_id
