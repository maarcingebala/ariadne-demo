from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from fastapi import FastAPI

from .schema import schema


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

app.mount("/graphql/", GraphQL(schema, websocket_handler=GraphQLTransportWSHandler()))
