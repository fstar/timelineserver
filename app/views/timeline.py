from flask_appbuilder import ModelView
from flask_appbuilder.base import AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app.models.timeline import TimeLine


class TimelineModelView(ModelView):
    datamodel = SQLAInterface(TimeLine)


def get_view(app_builder: AppBuilder):
    app_builder.add_view(
        TimelineModelView,
        "TimeLine",
        icon="fa-folder-open-o",
        category="TimeLine",
    )
