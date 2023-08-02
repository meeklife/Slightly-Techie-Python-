# import json
recipes = []


def create_recipe():
    name = input("Enter the recipe name: ")
    calories = input("Enter the amount of calories: ")
    duration = input("Enter the time to cook: ")
    recipe_id = len(recipes) + 1
    recipe = {
        "id": recipe_id,
        "name": name,
        "num_of_calories": calories,
        "cook_time": duration
    }
    recipes.append(recipe)
    print("=============================================")
    print(recipe["name"], "Recipe created successfully!")
    print("==============================================")

    with open("MyCookBook.txt", "w") as f:
        f.write(str(recipes))


def get_all_recipes():
    for recipe in recipes:
        with open("MyCookBook.txt", "r") as f:
            data = f.readlines(recipe)
        # print("============================")
        # # print(recipe["id"], recipe["name"])
        print(data["name"])
        # print("============================")


def get_recipe():
    recipeID = int(input("Enter the recipe ID: "))
    for recipe in recipes:
        if recipe["id"] == recipeID:
            print("============================")
            print(recipe["id"], recipe["name"])
            print("============================")
            return
    print("Recipe not found!")


def update_recipe():
    recipeID = int(input("Enter the recipe id to update: "))
    print("\nWhat do you want to update?")
    print("============================")
    print("1. The name\n")
    print("2. The number of calories\n")
    print("3. The cooking time\n")
    print("4. All\n")
    choice = int(input("Enter your option to update the recipe: "))

    for recipe in recipes:
        if recipe["id"] == recipeID:
            if choice == 1:
                new_name = input("Enter the new recipe name: ")
                recipe["name"] = new_name

            elif choice == 2:
                new_calories = input("Enter the new amount of calories: ")
                recipe["num_of_calories"] = new_calories

            elif choice == 3:
                new_duration = input("Enter the new time to cook: ")
                recipe["cook_time"] = new_duration

            print("======================================")
            print(f"{recipe} Recipe updated successfully!")
            print("=======================================")
            return
    print("Recipe not found!")


def delete_recipe():
    recipeID = int(input("Enter the recipe ID: "))
    for recipe in recipes:
        if recipe["id"] == recipeID:
            recipes.remove(recipe)
            print("============================================")
            print(recipe["name"], "Recipe deleted successfully!")
            print("============================================")
            return
    print("Recipe not found!")


def main():

    while True:
        print("Menu")
        print("1. Create a recipe\n")
        print("2. Get all recipes\n")
        print("3. Get a recipe\n")
        print("4. Update a recipe\n")
        print("5. Delete a recipe\n")
        print("6. Quit program\n")
        print(" ")
        choice = input("Enter your choice: ")
        print(" ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            get_all_recipes()
        elif choice == "3":
            get_recipe()
        elif choice == "4":
            update_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print(" Saved Goodbye")
            break


main()
