import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        exit()

def abilitys_type(pokemon_info: dict):
    abilitys = ""
    hidden_abilitys = ""
    for ability in range(len(pokemon_info["abilities"])):
        if pokemon_info["abilities"][ability]["is_hidden"]:
            if not hidden_abilitys:
                hidden_abilitys += pokemon_info["abilities"][ability]["ability"]["name"].replace("-", " ").capitalize()
            else:
                hidden_abilitys += ", " + pokemon_info["abilities"][ability]["ability"]["name"].replace("-", " ").capitalize()
        else:
            if not abilitys:
                abilitys += pokemon_info["abilities"][ability]["ability"]["name"].replace("-", " ").capitalize()
            else:
                abilitys += ", " + pokemon_info["abilities"][ability]["ability"]["name"].replace("-", " ").capitalize()
    return abilitys, hidden_abilitys

pokemon_name = input("The pokemon name: ").strip().lower()
pokemon_info = get_pokemon_info(pokemon_name)

name = pokemon_info["name"].capitalize()
id = pokemon_info["id"]
Type = pokemon_info["types"][0]["type"]["name"].capitalize()
category = pokemon_info["moves"][0]["move"]["name"].capitalize()
height_m = int(pokemon_info["height"]) / 10
height_f = str(round(height_m * 3.281, 2)).replace(".", "'") + "\""
weight_kg = int(pokemon_info["weight"]) / 10
weight_lbs = round(weight_kg * 2.205)
abilitys, hidden_abilitys = abilitys_type(pokemon_info)

print(f"Name: {name}")
print(f"ID: {id}")
print(f"Type: {Type}")
print(f"Category: {category}")
print(f"Height: {height_m:.1f} m ({height_f})")
print(f"Weight: {weight_kg:.1f} kg ({weight_lbs:.1f} lbs)")
print(f"Abilities: {abilitys}")
print(f"Abilities (Hidden): {hidden_abilitys}")