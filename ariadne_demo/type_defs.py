type_defs = """
    type Query {
        "Hello query."
        hello: String

        "Get all users."
        users: [User!]!

        "Get user by ID."
        user(id: ID!): User

        "Get all posts."
        posts: [Post!]!
    }

    type Mutation {
        "Create a new user."
        createUser(input: UserData!): CreateUserResponse!

        "Create a post."
        createPost(input: PostData!): CreatePostResponse!
    }

    type Subscription {
        feed: Post
        counter: Int!
    }

    "Represents a user."
    type User {
        "ID of an user."
        id: ID!

        "Email of an user."
        email: String!

        "Name of an user"
        name: String
    }

    "Input data for the creatUser mutation."
    input UserData {
        email: String!
        name: String
    }

    "Result of createUser mutation."
    type CreateUserResponse {
        error: String
        user: User
    }

    "Represents a post."
    type Post {
        "ID of a post."
        id: ID!

        "User who created a post."
        user: User!

        "Content of a post."
        content: String!

        "Creation date of a post."
        createdAt: String!
    }

    "Input data for createPost mutation."
    input PostData {
        user: ID!
        content: String!
    }

    "Result of createPost mutation."
    type CreatePostResponse {
        error: String
        post: Post
    }
"""
