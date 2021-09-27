# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Resource

from app.resources import Api
from app.schemas.timeline import TimeLineSchema
from app.service.timeline import TimeLineService


class TimeLineResource(Resource):

    def get(self) -> TimeLineSchema:
        timeline_service = TimeLineService()
        return timeline_service.get_all()


def get_resources():
    blueprint = Blueprint('timeline', __name__)
    api = Api(blueprint)
    api.add_resource(TimeLineResource, '/api/timeline')
    return blueprint
