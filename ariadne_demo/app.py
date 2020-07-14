from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def hello(*args, **kwargs):
    return JSONResponse({"Hello": "World"})


routes = [Route("/", hello)]

app = Starlette(routes=routes, debug=True)

