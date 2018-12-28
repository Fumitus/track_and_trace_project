from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

api_track_and_trace = Flask(__name__)
api = Api(api_track_and_trace)

PRODUCT_CODES = {}

def abort_if_product_code_doesnt_exist(product_code_id):
    if product_code_id not in PRODUCT_CODES:
        abort(404, message="TodoProduct_code {} doesn't exist".format(product_code_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# ProductCode
# shows a PRODUCT_CODES item and lets you to use items for box or pallet formation

class ProductCode(Resource):
    def get(self, product_code_id):
        abort_if_product_code_doesnt_exist(product_code_id)
        return PRODUCT_CODES[product_code_id]

    def delete(self, product_code_id):
        abort_if_product_code_doesnt_exist(product_code_id)
        del PRODUCT_CODES[product_code_id]
        return '', 204

    def put(self, product_code_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        PRODUCT_CODES[product_code_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks

class ProductCodeList(Resource):
    def get(self):
        return PRODUCT_CODES

    def post(self):
        args = parser.parse_args()
        product_code_id = int(max(PRODUCT_CODES.keys()).lstrip('todo')) + 1
        product_code_id = 'todo%i' % product_code_id
        PRODUCT_CODES[product_code_id] = {'task': args['task']}
        return PRODUCT_CODES[product_code_id], 201

##
## Actually setup the Api resource routing here
##

api.add_resource(ProductCodeList, '/product_code')
api.add_resource(ProductCode, '/product_code/<product_code_id>')


if __name__ == '__main__':
    api_track_and_trace.run(debug=True)