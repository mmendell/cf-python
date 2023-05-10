import pickle

def display_recipe(recipe):
    print('name: ', recipe['name'])
    print('cooking time overall', recipe['cooking_time'])
    print('ingredients: ', ', , '.join(recipe['ingredients']))
    print('difficulty: ', recipe['difficulty'])

def search_ingrediet(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('no. ', ingredient[0], ' ', ingredient[1])


    try:
        chosen_num = int(
            input('enter the number of your chosen ingredient: ')
        )
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()

    except IndexError:
        print('no such ingredient')
    except:
        print('some sort of error occured')

    else:
        for recipe in data['recipes_list']:
            if recpice_ing in recipe['ingredients']:
                if(recipe_ing == ingredient_searched):
                    print('\n this recipe contains your ingredient: ')
                    display_recipe(recipe)

filename = input('enter your file where your recipes are stored: ')
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print('file not found')
    data = {'recipes_list': [], 'all_ingredients': []}

else:
    search_ingrediet(data)

finally:
    recipes_file.close()
    