class Recipe():

    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ''

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_ingredients(self):
        return self.ingredients

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_difficulty(self):
        return self.difficulty

    def add_ingredient(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_ingredients()

    def get_ingredients(self):
        print("\nIngredients: ")
        print('----')
        for ingredient in self.ingredients:
            print('-' + str(ingredient))

    def calc_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'difficult'
        else:
            difficulty = 'unknown'
        return difficulty

    def search_ingredients(self, ingredients):
        for ingredient in ingredients:
            if ingredient in self.ingredients:
                return True
        return False

    def update_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def __str__(self):
        output = "Name: " + self.name + "\n" + \
            "Cooking time: " + str(self.cooking_time) + "\n" + \
            "Difficulty: " + self.difficulty + "\n" + \
            "Ingredients: " + str(self.ingredients) + "\n"
        for ingredient in self.ingredients:
            output += "- " + ingredient + "\n"
            return output

    def recipe_search(self, recipes):
        for recipe in recipes:
            if self.search_ingredients(recipe.ingredients):
                print(recipe)


recipes = []

coffee = Recipe("coffee")
coffee.add_ingredient("water", "coffee beans")
coffee.set_cooking_time(5)
coffee.set_name("coffee")
coffee.get_difficulty()
recipes.append(coffee)

cake = Recipe("cake")
cake.add_ingredient("flour", "sugar", "eggs", "butter")
cake.set_cooking_time(60)
cake.set_name("cake")
cake.get_difficulty()
recipes.append(cake)

soup = Recipe("soup")
soup.add_ingredient("water", "carrots", "potatoes", "onions")
soup.set_cooking_time(30)
soup.set_name("soup")
soup.get_difficulty()
recipes.append(soup)

print("recipes:")
print('--------')
for recipe in recipes:
    print(recipe)

print("searching for recipes with coffee")
coffee.recipe_search(recipes)

print("searching for recipes with potatoes")
soup.recipe_search(recipes)
