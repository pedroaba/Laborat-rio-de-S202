import pymongo
from dataset.pokemon_dataset import dataset


class Database:
    def __init__(self, database, collection):
        self._collection: pymongo.collection.Collection = None
        self._db = None
        self._cluster_connection = None

        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "localhost:64000"
            self._cluster_connection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self._db = self._cluster_connection[database]
            self._collection = self._db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def reset_database(self):
        try:
            self._db.drop_collection(self._collection)
            self._collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

    @property
    def collection(self) -> pymongo.collection.Collection:
        return self._collection
