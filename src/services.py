#Módulo que faza interface com o MongoDB e API do Twitter
from typing import Any, Dict, List

import tweepy

from src.connection import trends_collection
from src.constants import BR_WOE_ID
from src.secrets import ACESS_TOKEN, ACESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def get_trends(woe_id: int) -> List[Dict[str, Any]]:

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.get_place_trends(woe_id)

    return trends[0]["trends"]

def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)

def save_trends_mongo() -> None:
    trends = get_trends(woe_id=BR_WOE_ID)
    trends_collection.insert_many(trends)

def save_similar_mongo(trends : dict) -> None:
    trends_collection.insert_many(trends)


