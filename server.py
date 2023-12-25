from waitress import serve
from tapi_app.wsgi import application

if __name__ == '__main__':
    serve(application, port='8282')
   