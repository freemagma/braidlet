from flask import Flask
from braidlet import __version__


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    @app.route("/", methods=["GET", "POST"])
    def index():
        return f"Hello, World (v{__version__})!"

    return app