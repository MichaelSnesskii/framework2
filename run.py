from wsgiref.simple_server import make_server
from framework.main import Framework
from views import routes
from components import settings
#from urls import routes
import os
from components.front_controllers import front_controllers
from wsgi_static_middleware import StaticMiddleware


BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

app = Framework(routes, front_controllers)
app_static = StaticMiddleware(app,
                              static_root='staticfiles',
                              static_dirs=STATIC_DIRS)

with make_server('', 8282, app_static) as httpd:
    print("App running on port 8282...")
    httpd.serve_forever()
