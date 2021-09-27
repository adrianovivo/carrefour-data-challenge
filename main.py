from typing import List

from fastapi import FastAPI

from src.responses import TrendItem
from src.services import get_trends_from_mongo,save_trends_mongo,get_trends

app = FastAPI()  #https://fastapi.tiangolo.com/

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


if __name__ == "__main__":
    trends = get_trends_from_mongo()

    if not trends:
        save_trends_mongo()

