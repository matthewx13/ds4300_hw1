"""
J. Rachlin
Demonstration of working with Relational Database with python
"""

from dotenv import load_dotenv
import os
from tweet_mysql import TwitterAPI
from tweet_objects import Tweet
import pandas as pd
import random
import time

load_dotenv()


def main():
    # Authenticate
    api = TwitterAPI(os.environ["MYSQL_USER"], os.environ["MYSQL_PASS"], "twitterdb")

    # generate follows table
    follow = pd.read_csv("hw1_data/follows.csv")
    api.generate_follows_from_dataframe(follow)

    # insert tweets (1,000,000 / time --> inserts/sec)
    start = time.time()
    df_tweet = pd.read_csv("hw1_data/tweet.csv")

    # get Tweet object from row
    for _, row in df_tweet.iterrows():
        api.post_tweet(Tweet(user=row[0], ts=None, text=row[1]))
    insert_time = time.time() - start
    tweets_per_second = len(df_tweet) / insert_time
    print(f'Time = {round(time.time() - start, 4)} seconds')
    print(f'Tweets inserted per second = {round(tweets_per_second, 4)}')

    # get distinct users
    users = api.get_users()

    # get timelines (100 / time --> timelines/sec)
    timelines = []
    before = time.time()
    for _ in range(100):
        user = random.choice(users)  # randomize from distinct user list, then call api
        timelines.append(api.get_user_timeline(user))
    retrieve_time = time.time() - start
    timelines_per_second = len(timelines) / retrieve_time
    print(f'Time = {round(time.time() - before, 4)} seconds')
    print(f'User timelines retrieved per second = {round(timelines_per_second, 4)}')

if __name__ == '__main__':
    main()