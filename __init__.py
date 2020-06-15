from flask import Flask, request, render_template
from flask_restful import Resource, Api
from content_hash import Content

app = Flask(__name__)
api = Api(app)
data_con = Content()


class HomePage(Resource):
    @staticmethod
    def get():
        #return render_template('index.html')
        return 'Welcome to Site!'


class AddNode(Resource):
    @staticmethod
    def get(text):     # address_hash, content_hash
        a = text.strip().split(',')
        dict_a = {a[0].strip(): a[1].strip()}
        data_con.add_node(dict_a)
        return {'result': 'added'}


class ReadNode(Resource):
    @staticmethod
    def get(text):   # address_hash
        address = text.strip()
        response = data_con.read_node(address)
        return response


api.add_resource(HomePage, '/')
api.add_resource(AddNode, '/add/<text>')
api.add_resource(ReadNode, '/read/<text>')


# if __name__ == '__main__':
#     app.run(debug=True)
