from flask import Flask
from flask_restful import Api
from src.test import Test

app = Flask(__name__)
api = Api(app)

api.add_resource(Test, Test.route())

if __name__ == "__main__":
    app.run(host="0.0.0.0")