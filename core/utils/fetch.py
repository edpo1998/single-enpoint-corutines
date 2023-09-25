import asyncio
import httpx

class Fetch():
    """
        Clase  Fetch para extraccion de Data
    """
    def __init__(self,host,enpoint, items=None,visor_set=None) -> None:
        self._host = host
        self._enpoint = enpoint

    async def get_async(self,url):
        async with httpx.AsyncClient() as client:
            return await client.get(url)

    async def launch(self,n):
        getn = 25 - n
        resps = await asyncio.gather(*map(self.get_async, [f"{self._host}{self._enpoint}"]*getn))
        data = [resp.json() for resp in resps ]
        return data
    

