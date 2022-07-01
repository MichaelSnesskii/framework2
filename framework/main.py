import quopri
from framework.request import GetRequestClass

from os import path
from components.content_types import CONTENT_TYPES_MAP


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_applications = fronts_obj

    def __call__(self, environ, start_response):
        # адрес перехода
        path = environ['PATH_INFO']

        # закрывающий слеш, если нет
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        #обработка запроса с помощью контроллера
        method_class = GetRequestClass(method)
        data = method_class.get_request_params(environ)
        request[method_class.dict_value] = Framework.decode_value(data)
        print(f'{method}: {Framework.decode_value(data)}')

        #находит годный контроллер
        if path in self.routes_lst:
            view = self.routes_lst[path]

        else:
            view = PageNotFound404()

        for front_app in self.fronts_applications:
            front_app(environ, request)

        code, body = view(request)

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
