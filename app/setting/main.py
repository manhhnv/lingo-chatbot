import os
import motor.motor_asyncio
import pymongo


class AppSetting:
    def __init__(self, port=5000) -> None:
        self.mongo_url = os.environ.get('MONGO_URL')
        self.port = port
        self.client = pymongo.MongoClient(self.mongo_url)
        self.database = self.client["tuvung"]
        self.secret_key = os.environ.get('SECRET_KEY')
