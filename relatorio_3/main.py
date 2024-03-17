from random import randint

from database import Database
from relatorio_3.dataset.pokemon_dataset import dataset
from relatorio_3.pokedex import Pokedex

pokedex = Pokedex(database=Database)

pokemon = dataset[randint(0, len(dataset) - 1)]
pokedex.add_pokemon({
    **pokemon
})

print(pokedex.get_pokemon(pokemon["id"]))
print(pokedex.list_pokemons())
pokedex.update_pokemon(pokemon["id"], {
    **pokemon,
    "egg": "100km"
})

pokedex.remove_pokemon(pokemon["id"])
