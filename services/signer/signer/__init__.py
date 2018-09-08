from flask import Flask


def create_app(is_unit_test=False):
    app = Flask(__name__)

    if not is_unit_test:
        from dependency_config import container
        container.get_signer()

    from . import server
    app.register_blueprint(server.api)
    app.register_blueprint(server.signer, url_prefix='/signer')
    return app