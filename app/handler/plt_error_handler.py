import logging
import uuid
from flask import make_response

logger = logging.getLogger(__name__)


def bind_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(e):  # pylint: disable=W0612
        trace_id = uuid.uuid4().hex
        logger.error('error trace_id: %s', trace_id, exc_info=True)
        headers = {'X-ERROR-TRACE_ID': trace_id}
        if hasattr(e, 'code'):
            if hasattr(e, 'message'):
                return make_response(e.message, e.code, headers)
            elif hasattr(e, 'description'):
                return make_response(e.description, e.code, headers)
        return make_response(str(e), 500, headers)
