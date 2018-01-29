import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.user import UserRegister
from resources.products import VersionId, ProductList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sppdata'
api = Api(app)

#@app.before_first_request
#def create_tables():
#    db.create_all()

# import pdb; pdb.set_trace()
jwt = JWT(app, authenticate, identity) #/auth
# api.add_resource(Store, '/store/<string:name>')

api.add_resource(VersionId, '/versionid/<string:name>')
api.add_resource(ProductList, '/products')

api.add_resource(UserRegister, '/register')

# app.run(port=5000, debug=True)
if __name__ == '__main__':
    from db import db
    # with app.app_context():
    db.init_app(app)
    app.run(port=5000, debug=True)
