# web_app/__init__.py
from flask import Flask 

from webb_app.models import db, migrate
from webb_app.routes.home_routes import home_routes
from webb_app.routes.book_routes import book_routes
from webb_app.routes.twitter_routes import twitter_routes 

SQLALCHEMY_DATABASE_URI = "sqlite:////Users/noahpovis/Documents/GitHub/TwitOff2020/webb_app.db" # using relative filepath
#DATABASE_URL = "sqlite://///Users/noahpovis/Documents/GitHub/TwitOff2020/webb_app.db" # using absolute filepath on Mac (recommended)
#DATABASE_URL = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    return app 

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

