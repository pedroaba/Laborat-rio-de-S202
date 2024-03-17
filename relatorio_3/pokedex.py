import uuid
from typing import Type

from relatorio_3.database import Database
from relatorio_3.helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database: Type[Database]):
        self.database = database("pokedex", "pokemons")
        self.database.reset_database()

    def add_pokemon(self, pokemon: dict[str, str]):
        self.database.collection.insert_one(pokemon)
        writeAJson({
            "pokemon": pokemon,
            "operation": "insert"
        }, f'log-{uuid.uuid4()}')

    def remove_pokemon(self, pokemon_id: str):
        self.database.collection.delete_one({
            "id": pokemon_id
        })
        writeAJson({
            "pokemon_id": pokemon_id,
            "operation": "remove"
        }, f'log-{uuid.uuid4()}')

    def get_pokemon(self, pokemon_id: str):
        pokemon = self.database.collection.find_one({
            "id": pokemon_id
        })
        writeAJson({
            "pokemon": pokemon,
            "operation": "get_by_id"
        }, f'log-{uuid.uuid4()}')

        return pokemon

    def list_pokemons(self):
        pokemons = list(self.database.collection.find())
        writeAJson({
            "pokemons": pokemons,
            "operation": "list_all"
        }, f'log-{uuid.uuid4()}')

        return pokemons

    def update_pokemon(self, pokemon_id: str, pokemon: dict[str, str]):
        self.database.collection.update_one({
            "id": pokemon_id
        }, {
            "$set": pokemon
        }, upsert=True)

        writeAJson({
            "pokemon": pokemon,
            "pokemon_id": pokemon_id,
            "operation": "update_by_id"
        }, f'log-{uuid.uuid4()}')
