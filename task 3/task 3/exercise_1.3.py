recipes_list = []
ingredients_list = []


def take_recipe():
    name = str(input('what is the name of your dish?'))
    cooking_time = int(input('how long does it take to cook?'))
    ingredients = input('what ingredients does your recipe call for?')
    ingredients = ingredients.split()
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe


n = int(input('how many recipes would you like to enter?'))

for i in range(n):
    recipe = take_recipe()
    print(recipe)

    for ingredients in recipe['ingredients']:
        if ingredients not in ingredients_list:
            ingredients_list.append(ingredients)

    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['ease'] = 'difficult'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['ease'] = 'intermediate'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['ease'] = 'medium'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['ease'] = 'easy'

    print('-------------------------------')
    print('Recipe: ', recipe['name'])
    print('Cooking TIme: ', recipe['cooking_time'])
    print('Ingredients: ')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty level: ', recipe['ease'])

print('''Complete ingredient list
-----------------------------''')
ingredients_list = []
for recipe in recipes_list:
    for ingredient in recipe['ingredients']:
        ingredients_list.append(ingredient)
for i in ingredients_list:
    print(i)
