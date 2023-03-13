spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = [n['name'] for n in spicy_foods]
    return name_list

def get_spiciest_foods(spicy_foods):
    return [n for n in spicy_foods if n['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    return ([print(f"{n['name']} ({n['cuisine']}) | Heat Level: {n['heat_level']*'🌶'}") for n in spicy_foods])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food = [n for n in spicy_foods if n['cuisine'] == cuisine]
    return spicy_food

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass

get_spicy_food_by_cuisine(spicy_foods, "American")
