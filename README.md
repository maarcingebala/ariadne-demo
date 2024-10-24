Welcome to Ariadne Demo project! This is a simple app that shows basics of [Ariadne](http://ariadnegraphql.org/) framework.

# Installation guide

1. Install dependencies:

```shell
$ pip install poetry
$ poetry install --sync --no-root
```

2. In the project root directory run:

```shell
$ python run.py
```

The app should be running on `0.0.0.0:8000`. Go to `0.0.0.0:8000/graphql/` to access the GraphQL Playground.

# Next

Ideas for things to add next:

- JWT authentication, auth directives
- Add real database support
- Frontend app
