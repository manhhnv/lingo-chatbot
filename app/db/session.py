import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_URL'))
db = client.college

print(os.environ.get('MONGO_URL'))
