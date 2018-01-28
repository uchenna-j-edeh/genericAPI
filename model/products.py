
from db import db

from datetime import datetime
from model.dproducts import DependentProduct

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

class Snaps(db.Model):
   __tablename__ = "snaps"
   id = db.Column(db.Integer, primary_key=True)
   version_id = db.Column(db.String(40), unique=True, nullable=False)
   date_added = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

   dp = db.relationship('DependentProduct', lazy='select',
                        backref=db.backref('snaps', lazy='joined'))


   def __repr__(self):
      return '<Snaps %r>' % self.version_id

   @classmethod
   def remove_data(cls, name):
       dproducts = DependentProduct()
       products = Snaps()
       product = products.query.filter_by(version_id=name).first()

       if product:
           pid = product.id
           dproducts.query.filter_by(dp_id=pid).delete()
           products.query.filter_by(version_id=name).delete()
           db.session.commit()
           return True
       return False

   @classmethod
   def add_data(cls, data, name):
      vid = name
      dp_data = data['current']
      # try:
      plist = []
      for k, v in dp_data.items(): #unpack data
          item=DependentProduct(version_id=k, product_id=v[1], version=v[0])
          db.session.add(item)
          plist.append(item)

      item = Snaps(version_id=vid, dp=plist)
      db.session.commit()
