# Name: Jacob Steffen
# Description: Simple system for creating recipes, having cooks learn the recipes, and then show what kinds of recipes they've learned.

import random # for assigning recipe objects to Cooks

class Recipe:
    def __init__(self, name, ingredients, prep_time_minutes, cook_time_minutes):
        self.name = name
        self.ingredients = ingredients  # Expecting a list of ingredients
        self.prep_time_minutes = prep_time_minutes
        self.cook_time_minutes = cook_time_minutes

class Cook:
    def __init__(self, name):
        self.name = name
        self.__recipes_list = []  # List to store Recipe objects. 2 underscores makes it private

    def learn_recipe(self, recipe): # will only append a recipe if it isn't already in the list
        if recipe not in self.__recipes_list:
            self.__recipes_list.append(recipe)
        else:
            print(f"You already know how to cook {recipe.name}!")

    # Making this getter method lets the inherited class get access to the
    # private __recipes_list
    def get_recipes_list(self):
        return self.__recipes_list

    def display_recipes(self): # displays all the recipes a cook knows
        if not self.__recipes_list:
            print(f"{self.name} knows no recipes.")
            return
        print(f"{self.name}'s Recipes:")
        for recipe in self.__recipes_list:
            print(f"{recipe.name}:", end="\n\t") # adding \t to the end just so it looks nicer when printing
            for ingredient in recipe.ingredients:
                print(f"{ingredient} ", end='') # making end a space so it prints all on one line with seperation.
            print(f"\n\tPrep Time: {recipe.prep_time_minutes}")
            print(f"\tCook Time: {recipe.cook_time_minutes}")
            print(f"\tTotal Time: {recipe.prep_time_minutes + recipe.cook_time_minutes}")

    def display_recipe_complexity(self):
        count_of_simple_recipes = 0 
        count_of_complex_recipes = 0
        for recipe_obj in self.__recipes_list:
            if len(recipe_obj.ingredients) <= 4:
                count_of_simple_recipes += 1
            elif len(recipe_obj.ingredients) > 4:
                count_of_complex_recipes += 1
        
        print(f"{self.name} knows {count_of_simple_recipes} simple recipe(s) and {count_of_complex_recipes} complex recipe(s)")
        

class ExpertCook(Cook):
    def __init__(self, name, training_location): 
        super().__init__(name)
        self.training_location = training_location

    # same as the parent class except experts halve the prep time
    # You could come up with some clever ways of not rewriting similar code
    # using super, but in a short example like this it probably isn't worth going through that process.
    def display_recipes(self): 
            # because the recipe_list variable is private, ExpertCook doesn't
            # have access to it directly. Get it using a getter method.
            recipe_list = self.get_recipes_list()
            if not recipe_list: # If a list has nothing in it, this evalutes to True
                print(f"{self.name} knows no recipes.")
                return
            
            print(f"{self.name}'s Recipes (trained at {self.training_location}):")
            for recipe in recipe_list:
                print(f"{recipe.name}:", end="\n\t")
                for ingredient in recipe.ingredients:
                    print(f"{ingredient} ", end='')
        
                halved_prep_time = recipe.prep_time_minutes / 2
                print(f"\n\tPrep Time: {halved_prep_time} (Expert Speed)")
                print(f"\tCook Time: {recipe.cook_time_minutes}")
                print(f"\tTotal Time: {halved_prep_time + recipe.cook_time_minutes}")

# just making a lot of recipes
spaghetti = Recipe("Spaghetti", ["pasta", "tomato sauce", "meatballs"], 20, 10)
salad = Recipe("Salad", ["lettuce", "tomato", "cucumber", "salad dressing"], 10, 0)  # Assuming no cook time
pizza = Recipe("Pizza", ["pizza dough", "tomato sauce", "cheese", "pepperoni"], 15, 15)
chicken_curry = Recipe("Chicken Curry", ["chicken", "curry powder", "coconut milk", "rice"], 20, 25)
pancakes = Recipe("Pancakes", ["flour", "eggs", "milk", "sugar", "baking powder"], 5, 15)
chocolate_cake = Recipe("Chocolate Cake", ["flour", "cocoa powder", "eggs", "sugar", "butter"], 20, 30)
beef_stew = Recipe("Beef Stew", ["beef", "potatoes", "carrots", "onions", "beef broth"], 15, 105)

recipe_list = [spaghetti, salad, pizza, chicken_curry, pancakes, chocolate_cake, beef_stew]
cooks_list = []
while True:
    cook_name = input("Enter a cook's name: ")

    while True:
        cook_type = input(f"What type of cook is {cook_name}? (enter normal or expert): ").strip().lower()
        if cook_type == 'normal':
            cook_obj = Cook(cook_name)
            break
        elif cook_type == 'expert':
            training_loc = input(f"Where was {cook_name} trained? ")
            cook_obj = ExpertCook(cook_name, training_loc)
            break
        else:
            print("Not a valid cook type! Please enter normal or expert.\n")
    
    # outside of the inner loop
    cooks_list.append(cook_obj)
    print(f"{cook_name} has now been entered as a cook.")

    add_another_cook = input("Want to enter another cook? Enter 'Y' (or anything else) to keep going. Enter 'N' to stop: ").lower()

    if add_another_cook == 'n':
        break

for cook in cooks_list:
    # this means it will continue to try as long as the cook doesn't have 3 recipes
    # good for catching the case where you tried to add 3 recipes, but accidentaly add 2 of the same one.
    # notice I'm using a getter to check the list because the recipes list is private.
    while len(cook.get_recipes_list()) < 3: 
        cook.learn_recipe(random.choice(recipe_list))

for cook in cooks_list:
    cook.display_recipes() # run display on each of the cook/expertcooks that were made
    print() # just prints an extra space
    cook.display_recipe_complexity()
    print() # just adds an extra space
