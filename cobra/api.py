from flask import jsonify, make_response
from flask.ext import restful
from flask.ext.restful import reqparse
from cobra import app
from cobra.entry import EntryDAO

api = restful.Api(app)


class API(restful.Resource):
    entry_dao = EntryDAO()

    parser = reqparse.RequestParser()
    parser.add_argument('skip', type=int, help='Offset')
    parser.add_argument('limit', type=int, help='Limit')

    def get(self):

        array = []
        args = self.parser.parse_args()

        if args.skip is not None and args.limit is not None:
            entries = self.entry_dao.find({}, args.skip, args.limit)
            for entry in entries:
                del entry['_id']
                array.append(entry)

        return make_response(jsonify({'entries': array}))

#'/api/get/<int:skip>/<int:limit>'
api.add_resource(API, '/api/get')