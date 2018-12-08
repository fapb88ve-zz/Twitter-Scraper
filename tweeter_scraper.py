import pandas as pd
import requests
import tweepy
import secrets
from bs4 import BeautifulSoup

class TweetAPI():

    def __init__(self, k1,k2,k3,k4):
        self.key = k1
        self.secret_key = k2
        self.token = k3
        self.secret_token = k4

        auth = tweepy.OAuthHandler(self.key, self.secret_key)
        auth.set_access_token(self.token, self.secret_token)

        api = tweepy.API(auth, wait_on_rate_limit=True)
        self.api = api

    def user_information_getter(self, user_id):
        try:
            user_info = self.api.get_user(user_id)
        except:
            print('Unable to get user @{} info.'.format(user_id))

        return [user_id, user_info.followers_count, user_info.statuses_count]

    def tweet_getter(self, user_id, n):
        api = self.api
        tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.user_timeline, id = user_id).items(n):
                    url = "https://twitter.com/{}/status/{}".format(user_id, tweet.id_str)
                    page = requests.get(url)
                    page = BeautifulSoup(page.content, 'html.parser')
                    message_count = int(page.find('span',{"class":"ProfileTweet-actionCount"}).text.strip().split()[0])
                    temp = [user_id, tweet.created_at, tweet.id_str,
                            tweet.favorite_count, tweet.retweet_count, message_count, tweet.text]
                    tweets.append(temp)
            return tweets
        except:
            print("Unable to get user @{} tweets".format(user_id))
            pass


                #tweets.append()






if __name__ == '__main__':
    a = TweetAPI(secrets.key, secrets.secret_key, secrets.token, secrets.secret_token)
    #print(a.user_information_getter('PoleoRafael'))
    print(a.tweet_getter('PoleoRafael', 10))
