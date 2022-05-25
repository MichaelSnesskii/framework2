import quopri
from framework.request import GetRequests, PostRequests


class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # закрывающий слеш если нет
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'POST-request received: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'GET-parameters received: {request_params}')

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
