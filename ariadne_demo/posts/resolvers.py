from ariadne import ObjectType
from ..database import db

post = ObjectType("Post")

def resolve_posts(*_):
    return db.get_all_posts()


@post.field("user")
def resolve_post_user(post, _info):
    return db.get_user_by_id(post["user"])


def resolve_create_post(*_, input):
    error = None
    post = None
    try:
        post = db.create_post(input)
    except Exception as e:
        error = str(e)
    return {"error": error, "post": post}
