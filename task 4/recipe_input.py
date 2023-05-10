import pickle


def calc_difficulty(recipe):
    if recipe['Cooking_time'] < 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'easy'

    elif recipe['Cooking_time'] < 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'medium'

    elif recipe['Cooking_time'] >= 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'intermediate'

    elif recipe['Cooking_time'] >= 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'difficult'

    else:
        difficulty = 'unknown'
    return difficulty


def take_recipe():
    Name = input('enter the name of your recipe: ')
    Cooking_time = int(
        input('how long does it take to cook your stuff? ')
    )
    Ingredients = input('what stuff goes in this recipe? ')
    try:
        Ingredients = Ingredients.split()
        Ingredients = [Ingredient.lower() for Ingredient in Ingredients]
    except ValueError:
        print('Invalid ingredients')
        return
    recipe = {"Name": Name, 'Cooking_time': Cooking_time,
              'Ingredients': Ingredients}
    recipe['difficulty'] = calc_difficulty(recipe)
    return recipe


recipes_list = []
all_ingrediens = []

filename = input('enter your file with recipes name: ')

try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print('file not found, creating new file')
    data = {"recipes_list": [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num = int(input('how many recipes are ou loading? '))

for i in range(num):
    recipe = take_recipe()
    print(recipe)

    for Ingredient in recipe['Ingredients']:
        if Ingredient not in all_ingredients:
            all_ingredients.append(Ingredient)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = input('what do you want to call this file? ')
new_file_name = open(new_file_name, 'wb')
pickle.dump(data, new_file_name)
