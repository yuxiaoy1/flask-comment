import pytest
from flask import Flask
from flask import render_template_string

from flask_comment import Comment


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True

    @app.route('/')
    def index():
        return render_template_string('{{ comment.load() }}')

    return app


@pytest.fixture(autouse=True)
def comment(app):
    return Comment(app)


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
