import typing
import flask
import hashlib

from flask_restful import Resource, Api
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from werkzeug.exceptions import BadRequest

import application.api.models as _models


def register_blueprint(app):
    api_bp = flask.Blueprint('api',
                             __name__,
                             url_prefix=app.config.get('APPLICATION_ROOT', '') + '/v1',
                             static_folder='../static')
    api = Api(api_bp)

    api.add_resource(TestContent, '/test')
    app.register_blueprint(api_bp)


class TestContent(Resource):
    # Validation schema
    PRINT_CONTENT_JSONSCHEMA = {
        "type": "object",
        "properties": {
            "var1": {"type": "string"},
            "var2": {"type": "string"},
        },
        "required": ["var1", "var2"],
        "additionalProperties": False
    }

    def post(self):
        """Test api 1
        ---
        tags:
          - Test
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  var1:
                    type: string
                  var2:
                    type: string
                required:
                  - var1
                  - var2
        responses:
          '200':
            description: ok
        """
        # Now apply json schema validation
        r = TestContent.validate_json_schema(TestContent.PRINT_CONTENT_JSONSCHEMA,
                                             payload_expected=True)
        model = _models.Model1(**r)

        return flask.jsonify(model.build_rest())

    @staticmethod
    def validate_json_schema(schema, payload_expected=True):
        """
        Helper to validate json schema and perform basic non-null checks
        """
        r = flask.request.get_json()
        if payload_expected:
            if not r:
                raise BadRequest("JSON payload expected")
        else:
            if r is None:
                return {}

        # Now apply json schema validation
        try:
            validate(instance=r, schema=schema)
        except ValidationError as e:
            raise BadRequest("Invalid payload format - %s" % e.message)
        return r
