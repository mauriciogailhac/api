from flask import Flask
from flask_graphql import GraphQLView
from test.schema import schema
from test.models.models import db


def create_app():
    """
    create_app: function tu create flask app
    :return: flask app
    """
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
        """
        initialize_database: create database tables
        :return:
        """
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        shutdown_session: remove db session
        :param exception:
        :return:
        """
        db.session.remove()
    return app
