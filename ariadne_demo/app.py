from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from .schema import schema


async def hello(*args, **kwargs):
    return JSONResponse({"Hello": "World"})


routes = [Route("/", hello), Route("/graphql", GraphQL(schema=schema, debug=True))]

app = Starlette(routes=routes, debug=True)

