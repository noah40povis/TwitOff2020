# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify, request
from webb_app.models import db, User, Tweet, parse_records
from webb_app.services.twitter_service import api as twitter_api_client
from webb_app.services.basilica_service import basilica_connection

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    # fetching data from twitter api 

    twitter_user = twitter_api_client.get_user(screen_name) 
    # print("STATUSES COUNT:", len(tweets)) 

    

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)

    #update all attributes
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    
    #update in userbase
    db.session.add(db_user)
    db.session.commit()
    #breakpoint()
    statuses = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("TWEETS COUNT:", len(statuses))


     # Setting Basicilia API Connection to a variable
    basilica_api = basilica_connection

    # List Comprehension for set full_text of tweets to variable 
    all_tweet_texts = [status.full_text for status in statuses]
    # Creating embeddings for the full_text tweets via model="twitter"(basilica NLP model)
    embeddings = list(basilica_api.embed_sentences(all_tweet_texts, model="twitter"))
    # Printing the "len"(number) of embeddings
    print("NUMBER OF EMBEDDINGS:", len(embeddings))

    # TODO: explore using the zip() function maybe...
    # Setting counter for each specific tweet
    #counter = 0
    ## For Loop:
    # Looping through statuses and 
    for index, status in enumerate(statuses):
        # Printing the full-text of the tweets from the user_timeeline; 
        # specified above
        print(index)
        print(status.full_text)
        print("----")
        embedding = embeddings[index]
        
        #embedding = basilica_api.embed_sentence(status.full_text, model="twitter")
        # Get existing tweet from the DataBase or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.user.id #> or db_user.id
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        #counter+=1
    # Committing(saving) to the DataBase
    db.session.commit()
    
    
    return "I Love you. You are a great coder!"