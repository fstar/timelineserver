from flask import render_template

from flask_appbuilder import ModelView, BaseView, expose
from flask_appbuilder.base import AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app.models.timeline import SlideModel


class TimelineModelView(ModelView):
    datamodel = SQLAInterface(SlideModel)


class TimeLineView(BaseView):
    route_base = '/timeline'

    @expose('/')
    def index(self):
        return render_template('index.html')


def get_view(app_builder: AppBuilder):
    app_builder.add_view(
        TimelineModelView,
        'TimeLine',
        icon='fa-folder-open-o',
        category='TimeLine',
    )
    app_builder.add_view_no_menu(TimeLineView())
