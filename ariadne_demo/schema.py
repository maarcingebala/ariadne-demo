from ariadne import make_executable_schema, MutationType, ObjectType, QueryType

from .database import db


type_defs = """
    type Query {
        hello: String
        users: [User!]!
        user(id: ID!): User
        posts: [Post!]!
    }

    type Mutation {
        createUser(input: UserData!): CreateUserResponse!
        createPost(input: PostData!): CreatePostResponse!
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

    type Post {
        id: ID!
        user: User!
        content: String!
        createdAt: String!
    }

    input PostData {
        user: ID!
        content: String!
    }

    type CreatePostResponse {
        error: String
        post: Post
    }
"""


query = QueryType()
mutation = MutationType()

post = ObjectType("Post")
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


@query.field("posts")
def resolve_posts(*_):
    return db.get_all_posts()


@post.field("user")
def resolve_post_user(post, _info):
    return db.get_user_by_id(post["user"])


@mutation.field("createPost")
def resolve_create_post(*_, input):
    error = None
    post = None
    try:
        post = db.create_post(input)
    except Exception as e:
        error = str(e)
    return {"error": error, "post": post}


schema = make_executable_schema(type_defs, mutation, query, user, post)
