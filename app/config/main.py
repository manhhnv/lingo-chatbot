import os

def set_up():
    os.environ['FASTAPI_MODE'] = 'dev'
    os.environ['MONGO_URL'] = 'mongodb://localhost:27017/lingo'