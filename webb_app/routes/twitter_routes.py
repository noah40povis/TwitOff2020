# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify, request
from webb_app.models import db, User, Tweet, parse_records
from webb_app.services.twitter_service import api as twitter_api_client
# from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    # fetching data from twitter api 

    twitter_user = twitter_api_client.get_user(screen_name) 
    tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    # print("STATUSES COUNT:", len(tweets)) 

    

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)

    #update
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count

    db.session.add(db_user)
    db.session.commit()
    #breakpoint()
    return "OK"
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets