import os


def set_up():
    os.environ['FASTAPI_MODE'] = 'dev'
    os.environ['MONGO_URL'] = 'mongodb://localhost:27017'
    os.environ['SECRET_KEY'] = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
