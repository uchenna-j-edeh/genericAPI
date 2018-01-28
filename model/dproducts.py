from db import db

class DependentProduct(db.Model):

   __tablename__ = "dptable"
   id = db.Column(db.Integer, primary_key=True)
   version_id = db.Column(db.String(40), nullable=False)
   product_id = db.Column(db.String(40), nullable=False)
   version = db.Column(db.String(40), nullable=False)

   dp_id = db.Column(db.Integer, db.ForeignKey('snaps.id'),
        nullable=False)
