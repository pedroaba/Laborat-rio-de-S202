from typing import TypedDict

from bson import ObjectId

from relatorio_5.database import Database


"""
Validação do schema

{
    $jsonSchema: {
        bsonType: 'object',
        required: [
            titulo,
            autor,
            ano,
            preco
        ],
        properties: {
            titulo: {
                bsonType: 'string',
                description: 'deve ser uma string'
            },
            autor: {
                bsonType: 'string',
                description: 'deve ser uma string'
            },
            ano: {
                bsonType: 'int',
                description: 'deve ser uma string'
            },
            preco: {
                bsonType: 'float',
                description: 'deve ser uma string'
            },
        }
    }
}

"""


class BookDict(TypedDict):
    titulo: str
    autor: str
    ano: int
    preco: float


class Book:
    def __init__(self):
        self.database = Database("book", "books")

    def isert(self, book: BookDict):
        try:
            res = self.database.collection.insert_one(book)
            print(f"Book was inserted successfully: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Error: {e}")
            return None

    def find_by_id(self, _id: str):
        try:
            res = self.database.collection.find_one({"_id": ObjectId(_id)})
            print(f"Book found: {res}")
            return res
        except Exception as e:
            print(f"Error: {e}")
            return None

    def update_by_id(self, _id: str, book: BookDict):
        try:
            res = self.database.collection.update_one({"_id": ObjectId(_id)}, {"$set": book})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"Error: {e}")
            return None

    def delete_by_id(self, _id: str):
        try:
            res = self.database.collection.delete_one({"_id": ObjectId(_id)})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"Error: {e}")
            return None
