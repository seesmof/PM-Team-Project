from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_URI)
db = client.clicker

clients_collection = db.clients
