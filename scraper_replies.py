import csv
import tweepy
import ssl

#https://stackoverflow.com/questions/52307443/how-to-get-the-replies-for-a-given-tweet-with-tweepy-and-python

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = 'eC5TP6uUDa2s3MXXGaXvmLFmA'
consumer_secret = 'Oh1CFSAk0cfISybrw5rDe1g7WbeyWf0hARYnF5wEnsFegZtRD2'
access_token = '1397365651702829057-ExooHgpInX0DG0pj5CxPzsulufGXrX'
access_token_secret = '1UDeXdNey3jJIEiYLL4bnJfJ5wHRR0amv9v0daEeCUTlg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

### Redirect user to Twitter to authorize
##redirect_user(auth.get_authorization_url())

# Get access token
# Construct the API
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


name = '@StarTribune' #'therecount'
tweet_id = '1397978497902166020'
replies=[]
for tweet in tweepy.Cursor(api.search,q='to:{}'.format(name), since_id = tweet_id, tweet_mode='extended').items(50):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        #print("has replies")
        #print(tweet.in_reply_to_status_id_str)
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)
print(len(replies))
            
with open('replies.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)