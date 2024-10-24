import asyncio
import datetime


class DummyDatabase:
    """Dummy in-memory database."""

    users = [
        {"id": "1", "name": "John Doe", "email": "john@example.com",},
    ]

    posts = [
        {
            "id": "1",
            "user": "1",
            "content": "Ariadne is the best!",
            "createdAt": "2020-07-14 17:24:34.473455",
        }
    ]

    queue: asyncio.Queue = asyncio.Queue()

    def _get_next_id(self, db: list):
        return str(len(db) + 1)

    def get_all_users(self):
        """Return all users."""
        return self.users

    def get_user_by_id(self, user_id: str):
        """Lookup user by ID."""
        return next((user for user in self.users if user["id"] == user_id), None)

    def get_user_by_email(self, email: str):
        """Lookup user by email."""
        return next((user for user in self.users if user["email"] == email), None)

    def create_user(self, user_data: dict):
        """Creates a new user instance and saves it in the database.
        
        Raises exception a user with given email already exists.
        """
        email = user_data["email"]
        if self.get_user_by_email(email):
            raise Exception(f"User with this email already exists: {email}")

        user = dict(user_data)
        user["id"] = self._get_next_id(self.users)
        self.users.append(user)
        return user

    def get_all_posts(self):
        return self.posts

    def get_post_by_id(self, post_id: str):
        return next((post for post in self.posts if post["id"] == post_id), None)

    def create_post(self, post_data: dict):
        user_id = post_data["user"]
        if not self.get_user_by_id(user_id):
            raise Exception("User not found")

        post = dict(post_data)
        post["id"] = self._get_next_id(self.posts)
        post["createdAt"] = str(datetime.datetime.now())
        self.posts.append(post)
        self.queue.put_nowait(post)
        return post


db = DummyDatabase()
