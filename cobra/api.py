__author__ = '1000ch'

from flask.ext import restful
from flask.ext.restful import reqparse
from cobra import app
from cobra.entry import EntryDAO

api = restful.Api(app)

class API(restful.Resource):
  entryDao = EntryDAO()

  parser = reqparse.RequestParser()
  parser.add_argument('skip', type=int, help='Offset')
  parser.add_argument('limit', type=int, help='Limit')

  def get(self):

    list = []
    args = self.parser.parse_args()

    if args.skip is not None and args.limit is not None:
      list = self.entryDao.find({}, args.skip, args.limit)

    print(list)
    return {'entries': 0}

#'/api/get/<int:skip>/<int:limit>'
api.add_resource(API, '/api/get')