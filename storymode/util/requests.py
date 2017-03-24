from flask import Response
from flask.json import jsonify


class BadResponse(Response):
    def __init__(self, message, status_code=403):
        self.message = message
        self.status_code = status_code

    def to_json(self):
        return jsonify(
            type='error',
            message=self.message
        )
