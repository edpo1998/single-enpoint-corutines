from flask_restx import Api
from .modules.home import *

authorizations = {
    'token': {"type": "apiKey", "name": "Authorization", "in": "header"}
}
api = Api(
    title="Core Api",
    version="1.0",
    description= "API",
    authorizations=authorizations,
    security='Token',
    ordered=True
    )

api.prefix = '/api/v1'

api.add_namespace(enpointest,"/test")