
from flask_restx import Resource
from core.utils.fetch import Fetch
import asyncio
from . import api


@api.route('/')
class EnpointResource(Resource):
    
    def get(self):
        items = []
        seek_id = set()
        while len(items)<25:
            r = Fetch(host="https://api.chucknorris.io/",enpoint="jokes/random")
            items_response = asyncio.run(r.launch(len(items)))
            for item_n in items_response:
                if item_n['id'] not in seek_id:
                    items.append(item_n)
                    seek_id.add(item_n['id'])
        return items
