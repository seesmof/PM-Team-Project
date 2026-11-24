from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_URI)
database = client.get_database("clicks")
totals_collection = database.get_collection("totals")
