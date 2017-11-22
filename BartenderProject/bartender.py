from random import randint

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def getIngredients(tasteList):
    yourIngredients = []

    for taste in tasteList:
        print(questions.get(taste))
        ranNum = randint(0, len(ingredients.get(taste)) - 1)
        ingredient = ingredients.get(taste)[ranNum]
        yourIngredients.append(ingredient)
        print(" " + ingredient)
    return yourIngredients;


def getTastesFromUser():
    tasteList = []

    while True:
        taste = raw_input("Enter your taste('strong', 'salty', 'bitter', 'sweet', fruity or 'done' to complete): ")

        if (taste == "done"):
            break;

        if(questions.get(taste) == None):
            print("Your taste has not in list! ")
            continue

        tasteList.append(taste)
    return tasteList

yourTaste = getTastesFromUser()
yourIngredients = getIngredients(yourTaste)
print("Your Ingredients: ")
print(yourIngredients)