

def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# Get ingredient name
ingredient_name = not_blank("Ingredient name: ", "Please enter a valid response. Try again.")

