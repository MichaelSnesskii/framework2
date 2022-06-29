from wsgiref.simple_server import make_server
from framework.main import Framework
from views import routes
from components import settings
#from urls import routes

app = Framework(settings, routes)

with make_server('', 8282, app) as httpd:
    print("App running on port 8282...")
    httpd.serve_forever()
