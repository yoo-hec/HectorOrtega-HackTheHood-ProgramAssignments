food_price = {"chicken":1.59, "Beef":1.99, "cheese":1, "milk":2.50}
chicken_price = food_price ["chicken"]
beef_price = food_price ["Beef"]
cheese_price = food_price ["cheese"]
milk_price = food_price ["milk"]
print(food_price)


pokemon_pokedex_num = {"Charizard": 6, "Pikachu": 26, "Gyrados": 130, "Mewtwo":150}
Charizard_pokedex = pokemon_pokedex_num ["Charizard"]
Pikachu_pokedex = pokemon_pokedex_num ["Pikachu"]
Gyrados_pokedex = pokemon_pokedex_num ["Gyrados"]
Mewtwo_pokedex = pokemon_pokedex_num ["Mewtwo"]
pokemon_pokedex_num["Gengar"] = 94
pokemon_pokedex_num["Snorlax"] = 143
pokemon_pokedex_num["Dragonite"] = 149
del pokemon_pokedex_num["Pikachu"]
del pokemon_pokedex_num["Mewtwo"]
print (pokemon_pokedex_num)

shoe_count = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
shoe_count["SB Dunk"] -= 2
shoe_count["Yeezy"] += 1
shoe_count["Air Max"] += 7
shoe_count["Foamposite"] += 7
shoe_count["Jordan 13"] += 7
shoe_count["SB Dunk"] += 7
shoe_count["Yeezy"] += 7
shoe_count["Air Max"] -= 3
shoe_count["Foamposite"] -= 3
shoe_count["Jordan 13"] -= 3
shoe_count["SB Dunk"] -= 3
shoe_count["Yeezy"] -= 3
shoe_count["Jordan 1"] = 9
shoe_count["Air Forces"] = 14
shoe_count["Jordan 11"] = 11
del shoe_count["Foamposite"]
del shoe_count["Jordan 13"]
print (shoe_count)
