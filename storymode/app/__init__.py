from flask import Flask, request
from flask.json import jsonify
from storymode.util.requests import BadResponse
from storymode import models

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(None)


@app.route('/login', methods=['POST'])
def login():
    args = request.get_json()
    email, password = args['email'], args['password']
    user = models.user.find_by_email_and_password(email, password)
    if user:
        # todo: don't actually do this -- very insecure
        return jsonify(user)
    else:
        return BadResponse('Could not find that email or password.', 403)


@app.route('/signup', methods=['POST'])
def signup():
    args = request.get_json()
    email, password = args['email'], args['password']
    if models.user.find_by_email(args['email']):
        return BadResponse('A user with that email already exists.', 403)
    new_user = models.user.create_from_email(email=email, password=password)
    # todo: change this to some sort of cookie based response
    return jsonify(new_user)
