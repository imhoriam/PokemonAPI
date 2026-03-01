import requests

url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data():
    name = input("Enter a pokemon name: ")
    final_url = url + name
    response = requests.get(final_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Error code {response} ")



pokemon_data = get_pokemon_data()
print(pokemon_data["height"])