# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Resource

from app.resources import Api


class HelloWorld(Resource):

    def get(self):
        return 'hello world'


def get_resources():
    blueprint = Blueprint('Account', __name__)
    api = Api(blueprint)
    api.add_resource(HelloWorld, '/helloworld')
    return blueprint
