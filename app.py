﻿from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Api(Resource):
  def get(self):
    return "Hello World!"

api.add_resource(Api, '/')

if __name__ == '__main__':
  app.run(debug=True)