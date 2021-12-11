import os
import motor.motor_asyncio


class AppSetting:
    def __init__(self, port=5000) -> None:
        self.mongo_url = os.environ.get('MONGO_URL')
        self.port = port
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.mongo_url)
        self.db = self.client['tuvung']
        self.secret_key = os.environ.get('SECRET_KEY')
