from db import db

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from model.products import Snaps

class VersionId(Resource):
   parser = reqparse.RequestParser()
   parser.add_argument('current',
         type=dict,
         required=True,
         help="This filed cannot be left blank!"
   )

   def get(self, name):
      products = Snaps()
      product = products.query.filter_by(version_id=name).first()
      result = {}
      if product:
         for item in product.dp:
            result[item.version_id] = [item.version, item.product_id]
         return result, 200
      return {'message': "No item to GET."}, 404

   @jwt_required() #must autheticate before calling GET
   def post(self, name):
      # import pdb; pdb.set_trace()
      products = Snaps()
      product = products.query.filter_by(version_id=name).first()
      if product:
         return {'message': "An item with id '{}' already exists.".format(name)}, 400 # bad request

      data = VersionId.parser.parse_args()
      Snaps.add_data(data, name)
      return {'message': "Item successfuly POSTed"}, 201

      # except:
      #     return {"message": "An error occured inserting the item."}, 500 #Internal Server Error

   @jwt_required() #must autheticate before calling GET
   def delete(self, name):
      result = Snaps.remove_data(name)
      if result:
         return {'message': 'Item DELETED'}
      return {'message': 'Noting was deleted'}

   @jwt_required() #must autheticate before calling GET
   def put(self, name): # must be idempotent
      Snaps.remove_data(name)
      data = VersionId.parser.parse_args()
      Snaps.add_data(data, name)
      return {'message': "PUT action was successfuly."}, 201


class ProductList(Resource):

    def get(self):
        products = Snaps()
        return {item.version_id: str(item.date_added) for item in products.query.all()}
