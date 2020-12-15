from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kwood:@localhost/python-sample'
db = SQLAlchemy(app)

# Configure views
import sample.views


# Configure celery
def make_celery(flask_app: Flask) -> Celery:
    celery_app = Celery(
        flask_app.import_name,
        backend=flask_app.config['CELERY_RESULT_BACKEND'],
        broker=flask_app.config['CELERY_BROKER_URL'],
        include=['sample.tasks']
    )
    celery_app.conf.update(flask_app.config)

    class ContextTask(celery_app.Task):  # type: ignore
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celery = make_celery(app)
