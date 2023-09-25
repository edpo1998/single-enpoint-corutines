
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app=app, resources={ r"/api/v1/*": {"origins": "*"} })
from apis import api
api.init_app(app=app)


if __name__ == '__main__':

    app.run(port=8000)