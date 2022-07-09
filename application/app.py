import flask
from flask import Flask

import application.api as api
from application.extensions import swagger


def create_app(config_object="application.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    load_swagger_component_schemas(app)
    swagger.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    api.views.register_blueprint(app)

    @app.route('/')
    def home():
        return flask.redirect(app.config.get('APPLICATION_ROOT') + '/pages/apidocs', 307)

    return None


def load_swagger_component_schemas(app):
    swagger_config = app.config.get("SWAGGER", {})
    if 'components' not in swagger_config:
        swagger_config['components'] = {}
    if 'schemas' not in swagger_config['components']:
        swagger_config['components']['schemas'] = {}

    app.config['SWAGGER'] = swagger_config
