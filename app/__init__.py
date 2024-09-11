from flask import Flask

def create_app():
    app = Flask(__name__)

    # Secret key (xavfsizlik uchun zarur)
    app.config['SECRET_KEY'] = 'sizning_maxfiy_kalitingiz'

    from .routes import main
    app.register_blueprint(main)

    return app
