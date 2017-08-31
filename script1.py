from flask import Flask, render_template,request


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/success',methods =['POST'])
def success():
    if request.method == 'POST':
        word = request.form['tweet_ip']
        import tweepy
        from textblob import TextBlob
        consumer_key = "i18CUev4xKIu5JZMRHDGSke3y"
        consumer_secret = "1QBm0aaH34ibpME2xha6TmbVcX5KycYCae7zE1b4GXyLRfXqGD"

        access_token = "212248949-uVlZayfrrU6d9uzSG87Kiu53hukmojrdYTJ79BXX"
        access_token_secret = "fpqcALxBvat8sTjr4J5QShdTHgkx9Xqbjr5KygTPCtHPy"

        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        api = tweepy.API(auth)

        public_tweets = api.search(word)

        script1 = ""

        for tweet in public_tweets:
            script1 += "<p>"
            script1 += tweet.text
            analysis = TextBlob(tweet.text)
            script1 += "     " + str(analysis.sentiment.polarity)
            script1 += "</p>"

        return render_template("success.html",script1=script1)


if __name__=="__main__":
    app.run(debug=True)
