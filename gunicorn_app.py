import traceback
import gunicorn.app.base
import gunicorn.glogging
import logging

__version__ = '19.9.0.3'


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    DEFAULT_CONFIG = {
        'workers': 1,
        'threads': 10,
        'logger_class': 'gunicorn_app.Logger',
        'access_log_format': '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s',
    }

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        self.cfg.set('logger_class', 'gunicorn_app.Logger')
        for key, value in self.DEFAULT_CONFIG.items():
            key = key.lower()
            if key in self.cfg.settings:
                self.cfg.set(key, value)
        for key, value in self.options.items():
            key = key.lower()
            if key in self.cfg.settings:
                self.cfg.set(key, value)

    def load(self):
        return self.application


class Logger(gunicorn.glogging.Logger):

    def __init__(self, cfg):
        super().__init__(cfg)
        logging.getLogger('gunicorn.error').propagate = True
        logging.getLogger('gunicorn.access').propagate = True

    def access(self, resp, req, environ, request_time):
        """ See http://httpd.apache.org/docs/2.0/logs.html#combined
        for format details
        """
        # wrap atoms:
        # - make sure atoms will be test case insensitively
        # - if atom doesn't exist replace it by '-'
        safe_atoms = self.atoms_wrapper_class(self.atoms(resp, req, environ, request_time))

        try:
            self.access_log.info(self.cfg.access_log_format, safe_atoms)
        except Exception as _:
            self.error(traceback.format_exc())


def run_http_server(app, options: dict):
    app = StandaloneApplication(app, options)
    app.run()
