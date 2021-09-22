from flask import render_template
from flask_appbuilder import expose, AppBuilder, IndexView


class CustomeIndexView(IndexView):
    route_base = '/'

    @expose('/')
    def index(self):
        return render_template('index.html')


def get_view(app_builder: AppBuilder):
    app_builder.add_view_no_menu(CustomeIndexView())
