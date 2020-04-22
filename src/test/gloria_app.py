from flask import Flask
from flask_graphql import GraphQLView
from test.schema import schema
from config import Config
from flask_sqlalchemy import SQLAlchemy
from test.models.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(("config.ProductionConfig"))

    app.add_url_rule(
        '/gloria',
        view_func=GraphQLView.as_view(
            'gloria',
            schema=schema,
            graphiql=True
        )
    )
    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
    return app
