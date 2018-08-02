from TwitterAPI import TwitterAPI
import praw
from config import json_content


TW_CONSUMER_KEY = json_content['TW_CONSUMER_KEY']
TW_CONSUMER_SECRET = json_content['TW_CONSUMER_SECRET']
TW_ACCESS_TOKEN_KEY = json_content['TW_ACCESS_TOKEN_KEY']
TW_ACCESS_TOKEN_SECRET = json_content['TW_ACCESS_TOKEN_SECRET']

reddit = praw.Reddit(client_id=json_content['REDDIT_CLIENT_ID'],
                     client_secret=json_content['REDDIT_CLIENT_SECRET'],
                     password=json_content['REDDIT_PWD'],
                     user_agent='testscript by /u/ybce',
                     username='ybce')

subreddit = reddit.subreddit('coolguides')

def getTopPost():
    subs = subreddit.top(time_filter="day")
    top = subs.next()
    return top.title, top.url, top.shortlink


def tweet(event, context):
    api = TwitterAPI(TW_CONSUMER_KEY, TW_CONSUMER_SECRET, TW_ACCESS_TOKEN_KEY, TW_ACCESS_TOKEN_SECRET)

    title, url, shortlink = getTopPost()

    status = title+' '+url+' '+shortlink

    new_tweet = {"status": status}

    r = api.request("statuses/update", params=new_tweet)

    return r.json()


