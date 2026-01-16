from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Optional
from config.settings import settings


class MongoDBClient:

    _client: Optional[MongoClient] = None

    def __init__(self):
        if MongoDBClient._client is None:
            MongoDBClient._client = MongoClient(
                settings.mongo_uri,
                maxPoolSize=50,
                minPoolSize=5,
                serverSelectionTimeoutMS=5000
            )

        self._db: Database = MongoDBClient._client[settings.mongo_db]

    def get_database(self) -> Database:
        return self._db

    def get_collection(self, name: str) -> Collection:
        return self._db[name]

    def ping(self) -> bool:
        try:
            MongoDBClient._client.admin.command("ping")
            return True
        except Exception:
            return False

mongo_client = MongoDBClient()