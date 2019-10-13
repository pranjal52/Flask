from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


# Class Student inherits from the class Resource
class Student(Resource):
    # defining a simple get method
    def get(self, name):
        return {'student': name}


# Making the Student resource accessible via the API
# We do not need to define any @app.route for every method, instead the URLs are defined in the add_resource method.
api.add_resource(Student, '/student/<string:name>')

app.run(port=8080)
