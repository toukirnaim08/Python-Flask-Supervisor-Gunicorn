# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"

APPLICATION_ROOT = "/rest-service"

SWAGGER = {
    'title': 'Rest Service Testing',
    "version": "1.0.0",

    'uiversion': 3,
    'specs': [
        {
            'endpoint': 'apispec',
            'route':  APPLICATION_ROOT + '/rest/v1/apispec.json'
        }
    ],
    "specs_route": APPLICATION_ROOT + "/pages/apidocs/",
    'openapi': '3.0.2',
    "static_url_path": APPLICATION_ROOT + "/pages/flasgger_static",
    "doc_expansion": 'none',

    'components': {
        'schemas': {}
    },
}
