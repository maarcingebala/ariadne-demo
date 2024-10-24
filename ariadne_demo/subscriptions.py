import asyncio
from .database import db


async def feed_generator(obj, *_):
    while True:
        post = await db.queue.get()
        yield post


def resolve_feed(post, *_):
    return post


async def counter_generator(obj, *_):
    i = 0
    while True:
        await asyncio.sleep(1)
        yield i
        i += 1


def counter_resolver(count, *_):
    return count + 1