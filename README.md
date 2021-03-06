## Setup

1. Create a virtualenv using your tool of choice.
2. Run pip install -r requirements.txt.
3. In your terminal, run
    ```shell
    export FLASK_APP=sample
    export FLASK_ENV=development
    ```
4. To setup the db, in the same tab:

   ```shell
   alembic upgrade head
   ```

   Note: This is configured to use postgres on a machine with a user called `kwood`, so you'll need to
   update `sample.__init__.py` and `alembic.ini` to your username. You'll also need to have postgres running locally.
5. To run the app, in the same tab:
   ```shell
   flask run
   ```

## Paths

The paths of interest are:

1. `GET 127.0.0.1:5000` for a Hello World.
2. `GET 127.0.0.1:5000/users` for all users
3. `GET 127.0.0.1:5000/users/<username>` for a particular user
4. `POST 127.0.0.1:5000/users` to add a user. Your request must contain a JSON body with two fields like this:
   ```json
   {
      "username": "kwood",
      "email": "kwood@example.com",
      "first_name": "Kamal",
      "surname": "Wood"
   }
   ```
5. `PUT 127.0.0.1:500/users/<username>` to update the specified user. (Creating with this method isn't supported yet.)
   The body format is the same as the one for `POST /users`. You can only update the user's email address.

## Tasks

I use [Celery](https://flask.palletsprojects.com/en/1.1.x/patterns/celery/) for background tasks. Celery is configured to use redis on port 6379, so make sure you have a redis server running there. One way of doing that is with docker like this:

```shell
docker run -p 6379:6379 --name redis -d redis
```

You can then test the celery integration in the virtualenv with

```
export FLASK_APP=sample
flask shell
from sample.tasks import add_together
result = add_together.delay(1,1)
result.wait()
```

In a separate tab (also in the virtualenv), run

```shell
celery -A sample.celery worker --loglevel=DEBUG
```

And you should see the result (2) in the the first tab.

## Development

This project uses mypy for static type checking. Before committing any code, run `mypy sample` from the repo root and make sure that it returns no errors. See [the mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for help.
