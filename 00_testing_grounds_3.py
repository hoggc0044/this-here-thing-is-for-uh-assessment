# gotta, import the goods
import pandas


# functions go here
# recycled me num check from mmf mite
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Yeah nah, you need to put a number in.")


# say hello mite to me new yes_no thingy
def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("INCORRECT RESPONSE: Please correct your response in order to proceed. "
              "Missing argument: yes (y) / no (n). \n")


# currency formatting
def currency(x):
    return f"${x:.2f}"


# yeah, so uh this is my not_blank thing which uh makes sure there are no blank answers
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}. \nPlease try again. \n".format(error))
        else:
            valid = True
    return response


# ah yeh g'day mate uh this is my uh unit checker. it works hard at making sure you
# enter what should be entered.
def unit_checker(question):
    while True:
        response = input(question).lower()

        if response == "grams" or response == "g":
            return "grams"
        elif response == "kilograms" or response == "kg":
            return "kilograms"
        elif response == "millilitres" or response == "mL":
            return "millilitres"
        elif response == "litres" or response == "L":
            return "litres"
        elif response == "<blank>" or response == "BL":
            return "<blank>"
        elif response == "xxx":
            return "Next Question"
        else:
            print("Yeah, uh, I think it only accepts the following:\n"
                  " - grams or g\n"
                  " - kilograms or kg\n"
                  " - millilitres or mL\n"
                  " - litres or L\n"
                  " - <blank> or BL\n"
                  "It miiiiiiight be best if you used those instead of\n"
                  "whatever you put in...     Just a thought")


# main routine goes here
# Print introduction
print("************** INTRODUCTION *****************\n\n\n"
      "Welcome to the Recipe Cost Calculator!\n"
      "This calculator is a simple and easy to use tool for calculating a list of things\n"
      "you need to produce things like cakes or meals. Instructions have been created to\n"
      "show you how to use it. If you'd like to view the instructions, please answer\n"
      "the next question with a yes. If you'd like to give it a go without reading the\n"
      "instructions, then simply say no to the next question. I hope you enjoy using\n"
      "my calculator!\n\n\n"
      "************ READ INSTRUCTIONS? *************")

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    ****** Instructions ******

    Thank you for using my Recipe Cost Calculator!

    Using the calculator is simple! All you need to do is provide how many people you are serving,
    the names of the ingredients you are using (one by one, not all at once) and how much they are!
    It's essential that you provide the unit for each ingredient (i.e. flour; kg;) and the price of
    the item per unit (e.g $4 per kg), and the quantity of the ingredient (i.e. 4kgs of flour).

    The calculator will calculate all the provided information and will give you the total amount you'd
    need to produce whatever it is you are making for the amount of persons you have entered.
     The calculator will also write the information to a text file so it can be shared with other people.

    **************************
    ''')

# main routine
ingredient_name = []
ingredient_price = []
unit = []
required_amount = []
current_amount = []
creation_cost = []

# get recipe name
recipe_name = not_blank("What's the name of your recipe?", "Yeah nah, can't leave this blank.")
print()

# get serving size
serve = num_check("How many people are you serving?")
print()

print("Please enter your ingredients. You can type 'END' to move onto the next step.\n\n")

while True:
    # get ingredient
    get_ingredient = not_blank("Your ingredient is: ", "Yeah nah, error 404 - ingredient not found")
    print()

    if get_ingredient == "END" and len(ingredient_name) >= 3:
        break
    elif get_ingredient == "END" and len(ingredient_name) < 3:
        print("Yeah, nah, I think you need some more ingredients.")
        continue

    unit_response = unit_checker("What's the unit for this ingredient? \n"
                                 "Accepted: <blank>, kg, g, mL, L) \n")
    unit.append(unit_response)

    required = num_check("How much do you need? ")
    print()
    bought = num_check("How much did you buy?: ")
    print()
    price_per_unit = num_check("How much did you pay for it? $")
    print()

    unit_cost = (price_per_unit / bought * required)

    ingredient_name.append(get_ingredient)
    ingredient_price.append(price_per_unit)
    required_amount.append(required)
    current_amount.append(bought)
    creation_cost.append(unit_cost)

# WE MUST GIVE THE GOODS PANDAS FROM CHINA
recipe_dict = {
    "Ingredients": ingredient_name,
    "Ingredient Price": ingredient_price,
    "Unit": unit,
    "Required Amount": required_amount,
    "Current Amount": current_amount,
    "Creation Cost": creation_cost
}

recipe_panda = pandas.DataFrame(recipe_dict)


# cost of each serving and total cost
total_cost = recipe_panda["Creation Cost"].sum()
serving_cost = total_cost / serve

print('''\n
    **************************\n\n\n
Thank you for using my calculator.\n
This was made to allow people to include multiple recipes and ingredients. 


Your totals have been summed up and can be found below:\n
    **************************\n\n\n
''')
print(recipe_panda)
print("Total Cost: ${:.2f}".format(total_cost))
print("Cost per Serving: ${:.2f}".format(serving_cost))


