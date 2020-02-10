
from wsgiref.simple_server import make_server

from hello import application


print('Serving HTTP on port 8000...', flush=True)
httpd = make_server('', 8000, application)


httpd.serve_forever()