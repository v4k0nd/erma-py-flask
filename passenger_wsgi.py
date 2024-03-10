# import imp
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'app.py')
# application = wsgi.app

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
import os

# Import your Flask app
from app import app as flask_app

app_base_url = os.environ.get("APP_BASE_URL", "")


# Create a simple app that returns a 404 response
def simple_app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    print("Request Path:", path)  # Log request path
    response = Response("Not Found", status=404)
    return response(environ, start_response)


# Apply DispatcherMiddleware
application = DispatcherMiddleware(simple_app, {app_base_url: flask_app})
