import os
from pymongo import MongoClient


class BaseMongo:
    def __init__(self) -> None:
        self.client = MongoClient(os.getenv("mongo_connection_string"))
        self.db = self.client['apt_api']

