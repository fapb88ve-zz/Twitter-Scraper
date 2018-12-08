import pandas as pd
import requests
import tweepy
import secrets

class TweetAPI():

    def __init__(self, k1,k2,k3,k4):
        self.key = k1
        self.secret_key = k2
        self.token = k3
        self.secret_token = k4

        auth = tweepy.OAuthHandler(self.key, self.secret_key)
        auth.set_access_token(self.token, self.secret_token)

        api = tweepy.API(auth)
        self.api = api

    def user_information_getter(self, user_id):
        try:
            user_info = self.api.get_user(user_id)
        except:
            print('Unable to get user @{} info.')

        return [user_id, user_info.followers_count, user_info.statuses_count]


if __name__ == '__main__':
    a = TweetAPI(secrets.key, secrets.secret_key, secrets.token, secrets.secret_token)
    print(a.user_information_getter('PoleoRafael'))
