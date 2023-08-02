class Recipe:
    def __init__(self, name, num_of_calories, cook_time):
        self.id = 0  # Placeholder for the recipe id
        self.name = name
        self.num_of_calories = num_of_calories
        self.cook_time = cook_time


class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.next_recipe_id = 1

    def create_recipe(self):
        name = input("Enter the name of the recipe: ")
        num_of_calories = int(input("Enter the number of calories: "))
        cook_time = int(input("Enter the cook time (in minutes): "))

        recipe = Recipe(name, num_of_calories, cook_time)
        recipe.id = self.next_recipe_id
        self.next_recipe_id += 1

        self.recipes.append(recipe)
        print("Recipe created successfully!")

        with open("MyCookBook.txt", "a") as f:
            f.write(str(recipe))

    def get_all_recipes(self):
        for recipe in self.recipes:
            print(
                f"Recipe ID: {recipe.id}, Name: {recipe.name}, Calories: {recipe.num_of_calories}, Cook Time: {recipe.cook_time}")

    def get_recipe_by_id(self):
        recipe_id = int(input("Enter the recipe id: "))
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                print(
                    f"Recipe ID: {recipe.id}, Name: {recipe.name}, Calories: {recipe.num_of_calories}, Cook Time: {recipe.cook_time}")
                return
        print("Recipe with the specified id cannot be found.")

    def update_recipe_by_id(self):
        recipe_id = int(input("Enter the recipe id: "))
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                name = input("Enter the updated name of the recipe: ")
                num_of_calories = int(
                    input("Enter the updated number of calories: "))
                cook_time = int(
                    input("Enter the updated cook time (in minutes): "))
                recipe.name = name
                recipe.num_of_calories = num_of_calories
                recipe.cook_time = cook_time
                print("Recipe updated successfully!")
                return
        print("Recipe with the specified id cannot be found.")

    def delete_recipe_by_id(self):
        recipe_id = int(input("Enter the recipe id: "))
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                self.recipes.remove(recipe)
                print("Recipe deleted successfully!")
                return
        print("Recipe with the specified id cannot be found.")


def main():
    recipe_manager = RecipeManager()

    while True:
        print("\nMain Menu:")
        print("1. Create a Recipe")
        print("2. Get all Recipes")
        print("3. Get a Recipe")
        print("4. Update a Recipe")
        print("5. Delete a Recipe")
        print("6. Quit Program")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            recipe_manager.create_recipe()
        elif choice == 2:
            recipe_manager.get_all_recipes()
        elif choice == 3:
            recipe_manager.get_recipe_by_id()
        elif choice == 4:
            recipe_manager.update_recipe_by_id()
        elif choice == 5:
            recipe_manager.delete_recipe_by_id()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main()
