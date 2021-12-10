import os


class AppSetting:
    def __init__(self, port=5000) -> None:
        self.mongo_url = os.environ.get('MONGO_URL')
        self.port = port
