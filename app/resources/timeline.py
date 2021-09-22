# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Resource

from app.resources import Api
from app.schema.timeline import TimeLineJson


class TimeLineResource(Resource):

    def get(self) -> TimeLineJson:
        time_line_json = TimeLineJson(events=[
            TimeLineJson.Slide(start_date=TimeLineJson.Slide.Date(year=2009),
                               end_date=TimeLineJson.Slide.Date(year=2020),
                               text=TimeLineJson.Slide.Text(headline='aaaaa', text='asdasdasasdadaasda')),
            TimeLineJson.Slide(start_date=TimeLineJson.Slide.Date(year=2010),
                               end_date=TimeLineJson.Slide.Date(year=2021),
                               text=TimeLineJson.Slide.Text(headline='bbbbb', text='bbbbbbbbbbbbbbbbb'))
        ])
        return time_line_json


def get_resources():
    blueprint = Blueprint('timeline', __name__)
    api = Api(blueprint)
    api.add_resource(TimeLineResource, '/api/timeline')
    return blueprint
