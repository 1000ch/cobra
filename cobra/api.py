__author__ = '1000ch'

from flask.ext import restful
from cobra import app
from cobra.store import Store

api = restful.Api(app)

class API(restful.Resource):
  def get(self, skip):
    list = Store().find({}, skip, 20)
    return list

api.add_resource(API, '/api/<int:skip>')