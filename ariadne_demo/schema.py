from ariadne import (
    make_executable_schema,
    MutationType,
    SubscriptionType,
    QueryType,
)

from . import subscriptions
from .type_defs import type_defs
from .posts import resolvers as post_resolvers
from .users import resolvers as user_resolvers


# Root types
mutation = MutationType()
subscription = SubscriptionType()
query = QueryType()


# Example query resolver
@query.field("hello")
def resolve_hello(*_):
    return "World"


# Post resolvers
query.set_field("posts", post_resolvers.resolve_posts)
mutation.set_field("createPost", post_resolvers.resolve_create_post)


# User resolvers
query.set_field("users", user_resolvers.resolve_users)
query.set_field("user", user_resolvers.resolve_user)
mutation.set_field("createUser", user_resolvers.resolve_create_user)


# Subscriptions
subscription.set_field("counter", subscriptions.counter_resolver)
subscription.set_source("counter", subscriptions.counter_generator)
subscription.set_field("feed", subscriptions.resolve_feed)
subscription.set_source("feed", subscriptions.feed_generator)


# Gather all types
types = [mutation, subscription, query, user_resolvers.user, post_resolvers.post]


# Expose the schema object
schema = make_executable_schema(type_defs, *types)
