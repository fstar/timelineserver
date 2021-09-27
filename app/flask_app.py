import logging

from flask import Flask
from flask_appbuilder.base import AppBuilder
from flask_compress import Compress

from app.encoder.plt_json_encoder import PltJSONEncoder
from app.handler.plt_error_handler import bind_error_handlers

logger = logging.getLogger(__name__)


def bind_app_hook(app):
    """
    绑定请求前后钩子
    :param app: Flask App实例
    :return:
    """

    @app.before_request
    def before_request():  # pylint: disable=W0612,W0613
        return

    @app.after_request
    def cors_after_request(resp):  # pylint: disable=W0612,W0613
        resp.headers.set('Access-Control-Allow-Origin', '*')
        resp.headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        resp.headers.set('Access-Control-Allow-Headers',
                         'Response-Language, Content-Type, Cache-Control, Authorization, X-Requested-With')
        return resp

    @app.teardown_request
    def flask_teardown(exception):  # pylint: disable=W0612,W0613
        return


def bind_api(app: Flask):
    from app.resources import hello_world, timeline
    # 注册 api
    blueprints = (hello_world.get_resources(), timeline.get_resources())
    for bp in blueprints:
        app.register_blueprint(bp)


def bind_views(app_builder: AppBuilder):
    from app.views import timeline
    # 绑定 view
    views = (timeline,)
    for v in views:
        v.get_view(app_builder)


def create_app():
    from app.database import init_db

    app = Flask(__name__, static_folder='./statics', template_folder='./template')
    Compress(app)

    app._logger = logging.getLogger(__name__)  # pylint: disable=protected-access
    app.config['RESTFUL_JSON'] = {'cls': PltJSONEncoder}
    app.json_encoder = PltJSONEncoder
    app_builder = init_db(app)

    # 绑定全局异常处理器、请求前后钩子、默认终端等
    bind_app_hook(app)
    bind_error_handlers(app)

    bind_api(app)
    bind_views(app_builder)

    app.url_map.strict_slashes = False

    return app


flask_app = create_app()
