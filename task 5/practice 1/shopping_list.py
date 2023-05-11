# class ShoppingList(object):
#     def __init__(self, list_name):
#         self.list_name = list_name
#         self.shopping_list = []

#     def add_item(self, item):
#         if item not in self.shopping_list:
#             self.shopping_list.append(item)

#     def remove_item(self, item):
#         if item in self.shopping_list:
#             self.shopping_list.remove(item)

#     def view_list(self):
#         print(self.shopping_list)


#     def merge_lists(self, obj):
#         merged_lists_name = 'merged list - ' + \
#             str(self.list_name) + " + " + str(obj.list_name)
#         merged_lists_obj = ShoppingList(merged_lists_name)

#         merged_lists_obj.shoppiing_list = self.shopping_list.copy()

#         for item in obj.shopping_list:
#             if not item in merged_lists_obj.shopping_list:
#                 merged_lists_obj.shopping_list.append(item)

#             return merged_lists_obj


# pet_store_list = ShoppingList('Pet Store shopping list')
# grocery_store_list = ShoppingList('Grocery Store shopping list')


# pet_store_list.add_item('dog food')
# pet_store_list.add_item('cat food')
# pet_store_list.add_item('flea collars')
# pet_store_list.add_item('dog bed')
# pet_store_list.add_item('cat bed')

# for item in ['fruits', 'vegetable', 'bowl', 'ice cream']:
#     grocery_store_list.add_item(item)
# pet_store_list.merge_lists(grocery_store_list)


# pet_store_list.remove_item('flea collars')
# pet_store_list.add_item('frisbee')

# merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# merged_list.view_list()


class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + ' feet ' + str(self.inches) + ' inches'
        return output
    

    def __add__(self, other):
        # converting height to inches
        height_A_inches = self.feet * 12 + self.inches
        height__B__inches = other.feet * 12 + other.inches
        total_height_inches = height_A_inches + height__B__inches
        total_feet = total_height_inches // 12
        output_inches = total_height_inches -(total_feet * 12)
        return Height(total_feet, output_inches)
person_A_height = Height(5, 11)
person_B_height = Height(6, 2)
height_sum = person_A_height + person_B_height

print("sum ofheihgts ", height_sum) 