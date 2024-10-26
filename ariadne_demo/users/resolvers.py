from ariadne import ObjectType

from ..database import db

user = ObjectType("User")


def resolve_users(obj, info, **kwargs):
    return db.get_all_users()


def resolve_user(*_, **kwargs):
    user_id = kwargs["id"]
    return db.get_user_by_id(user_id)


@user.field("posts")
def resolve_posts(obj, info, **kwargs):
    return db.get_posts_by_user_id(obj["id"])


def resolve_create_user(*_, input):
    error = None
    user = None
    try:
        user = db.create_user(input)
    except Exception as e:
        error = str(e)
    return {"error": error, "user": user}