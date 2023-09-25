
from flask import Flask
from flask_cors import CORS


def make_app():
    app = Flask(__name__)
    cors = CORS(app=app, resources={ r"/api/v1/*": {"origins": "*"} })
    from apis import api
    api.init_app(app=app)
    return app

if __name__ == '__main__':
    app = make_app()
    app.run(port=8000,host='0.0.0.0')