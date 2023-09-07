import pandas

ingredient_name = []
ingredient_price = []
unit = []
required_amount = []
current_amount = []
creation_cost = []


recipe_dict = {
    "Ingredients": ingredient_name,
    "Price": ingredient_price,
    "Unit": unit,
    "Needed": required_amount,
    "Bought": current_amount,
    "Cost": creation_cost
}

recipe_panda = pandas.DataFrame(recipe_dict)

print(recipe_panda)