from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from .schema import schema


app = Starlette(debug=True)
app.mount("/", GraphQL(schema=schema, debug=True))
