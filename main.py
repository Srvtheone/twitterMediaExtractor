from html import entities
from flask import Flask, request, render_template
from tweepy import Cursor, OAuthHandler, API

consumer_key = "Qn1AIINYtjBPln4xZrV4S1nOb" 
consumer_key_secret = "SwL1yOk4kMAujQlGICKWevJX4zbmbisJWfDFbTxKtMT8wcXT4F"

app = Flask(__name__)

get_authentication = OAuthHandler(consumer_key, consumer_key_secret)
api = API(get_authentication)

def get(query, num_tweets):
    url = []

    tweets = Cursor(api.search_tweets, query).items(num_tweets)

    for tweet in tweets:    
        if "media" in tweet.entities:
            url.append(tweet.entities['media'][0]['media_url'])

    return url

@app.route("/", methods = ["GET", "POST"])
def home():
    if(request.method=="POST"):
        query = request.form["query"]
        images = get(query, 50)
        return render_template('home.html', images = images)
    else:
        return render_template("enter.html")


if __name__ == '__main__':
    app.run(debug=True) 



