from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    
    db.init_app(app)


    from .views import main
    app.register_blueprint(main)
    return app

application = create_app()