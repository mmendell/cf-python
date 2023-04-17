import pickle

def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'easy'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'medium'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'intermediate'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'difficult'
    return difficulty

def take_recipe():
    name =input('enter the name of your recipe')
    cooking_time = int(
        input('how long does it take to cook your stuff? ')
    )
    ingredients = input('what stuff goes in this recipe? ')
    ingredients = ingredients.split()
    ingredients = [ingredient.lower() for ingredient in ingredients]
    recipe = {"Name": name, 'cooking_time': cooking_time, 'ingredients': ingredients}
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
    data = {"recipes_list":[], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num = int(input('how many recipes are ou loading? '))

for i in range(num):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = { 'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = input('what do you want to call this file? ')
with open(new_file_name, 'wb') as f:
    pickle.dump(data, f)