import pickle


def display_recipe(recipe):
    print('Name:', recipe['Name'])
    print('Cooking time overall:', recipe['Cooking_time'])
    print('Ingredients:', ', '.join(recipe['Ingredients']))
    print('Difficulty:', recipe['difficulty'])


def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('no.', ingredient[0], '-', ingredient[1])

    try:
        chosen_num = int(input('Enter the number of your chosen ingredient: '))
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()

    except IndexError:
        print('No such ingredient')
    except:
        print('Some sort of error occurred')

    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['Ingredients']:
                print('\nThis recipe contains your ingredient:')
                display_recipe(recipe)
                break
        else:
            print('No recipe found with the chosen ingredient')


filename = input('Enter the file where your recipes are stored: ')
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)

    search_ingredient(data)  # Moved the function call inside the try block

except FileNotFoundError:
    print('File not found')
    data = {'recipes_list': [], 'all_ingredients': []}

except Exception as e:  # Added a generic exception block to catch any other errors
    print('An error occurred:', e)

finally:
    recipes_file.close()
