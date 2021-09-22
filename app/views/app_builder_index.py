from flask_appbuilder import IndexView, AppBuilder


class AppIndexView(IndexView):
    route_base = "/app"


def get_view(app_builder: AppBuilder):
    app_builder.indexview = AppIndexView
