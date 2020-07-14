class DummyDatabase:
    """Dummy in-memory database."""

    users = [
        {"id": "1", "name": "John Doe", "email": "john@example.com",},
    ]

    def _get_next_id(self):
        return str(len(self.users) + 1)

    def get_all_users(self):
        """Return all users."""
        return self.users

    def get_user_by_id(self, user_id):
        """Lookup user by ID."""
        return next((user for user in self.users if user["id"] == user_id), None)

    def get_user_by_email(self, email):
        """Lookup user by email."""
        return next((user for user in self.users if user["email"] == email), None)

    def create_user(self, user_data):
        """Creates a new user instance and saves it in the database.
        
        Raises exception a user with given email already exists.
        """
        email = user_data["email"]
        if self.get_user_by_email(email):
            raise Exception(f"User with this email already exists: {email}")

        user = dict(user_data)
        user["id"] = self._get_next_id()
        self.users.append(user)
        return user


db = DummyDatabase()
