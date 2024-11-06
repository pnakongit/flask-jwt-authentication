from flask import Flask, jsonify, Response


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index() -> Response:
        return jsonify(message="Hi from the home route")

    return app
