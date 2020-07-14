from ariadne import make_executable_schema, MutationType, ObjectType, QueryType

from .database import db


type_defs = """
    type Query {
        hello: String
        users: [User!]!
        user(id: ID!): User
    }

    type Mutation {
        createUser(input: UserData!): CreateUserResponse!
    }

    type User {
        id: ID!
        email: String!
        name: String
    }

    input UserData {
        email: String!
        name: String
    }

    type CreateUserResponse {
        error: String
        user: User
    }
"""


mutation = MutationType()
query = QueryType()
user = ObjectType("User")


@query.field("hello")
def resolve_hello(*_):
    return "World"


@query.field("users")
def resolve_users(*_):
    return db.get_all_users()


@query.field("user")
def resolve_user(*_, **kwargs):
    user_id = kwargs["id"]
    return db.get_user_by_id(user_id)


@mutation.field("createUser")
def resolve_create_user(*_, input):
    error = None
    user = None
    try:
        user = db.create_user(input)
    except Exception as e:
        error = str(e)
    return {"error": error, "user": user}


schema = make_executable_schema(type_defs, mutation, query, user)
