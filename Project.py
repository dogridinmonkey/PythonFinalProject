from Tables import Recipe, Ingredient, Category, User


def main_menu():
    print("\n\033[94mMain Menu\033[0m")
    print("1. Recipes")
    print("2. Ingredients")
    print("3. Categories")
    print("4. Users")
    print("5. Exit")
    choice = input("Enter number of your choice: ")
    return choice


def recipe_menu():
    print("\n\033[94mRecipe Menu\033[0m")
    print("1. Add a recipe")
    print("2. Update a recipe")
    print("3. Display a recipe")
    print("4. Display all recipes")
    print("5. Delete a recipe")
    print("6. Main Menu")
    choice = input("Enter number of your choice: ")
    return choice


def ingredient_menu():
    print("\n\033[94mIngredient Menu\033[0m")
    print("1. Add an ingredient")
    print("2. Update an ingredient")
    print("3. Display an ingredient")
    print("4. Display all ingredients")
    print("5. Delete an ingredient")
    print("6. Main Menu")
    choice = input("Enter number of your choice: ")
    return choice


def category_menu():
    print("\n\033[94mCategory Menu\033[0m")
    print("1. Add a category")
    print("2. Update a category")
    print("3. Display all categories")
    print("4. Delete a category")
    print("5. Main Menu")
    choice = input("Enter number of your choice: ")
    return choice


def user_menu():
    print("\n\033[94mUser Menu\033[0m")
    print("1. Add a user")
    print("2. Update a user")
    print("3. Display a user")
    print("4. Display all users")
    print("5. Delete a user")
    print("6. Main Menu")
    choice = input("Enter number of your choice: ")
    return choice


def main():
    print("\n\033[94m** Welcome to the Recipe Database **\033[0m")
    while True:
        main_choice = main_menu()
        if main_choice == "1":
            while True:
                recipe_choice = recipe_menu()
                r = Recipe("recipeDB.sqlite")
                if recipe_choice == "1":
                    fields, values = r.input_data()
                    r.create_record('recipes', fields, values)
                elif recipe_choice == "2":
                    recipe_id = input("Enter the id of the recipe to update: ")
                    fields, values = r.input_data()
                    r.update_record('recipes', 'recipe_id', recipe_id, fields, values)
                elif recipe_choice == "3":
                    recipe_id = input("Enter the id of the recipe to display: ")
                    r.read_record('recipes', 'recipe_id', recipe_id)
                elif recipe_choice == "4":
                    r.read_all_records('recipes')
                elif recipe_choice == "5":
                    recipe_id = input("Enter the id of the recipe to delete: ")
                    r.delete_record('recipes', 'recipe_id', recipe_id)
                elif recipe_choice == "6":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice")
        elif main_choice == "2":
            while True:
                ingredient_choice = ingredient_menu()
                i = Ingredient("recipeDB.sqlite")
                if ingredient_choice == "1":
                    fields, values = i.input_data()
                    i.create_record('ingredients', fields, values)
                elif ingredient_choice == "2":
                    ingredient_id = input("Enter the id of the ingredient to update: ")
                    fields, values = i.input_data()
                    i.update_record('ingredients', 'ingredient_id', ingredient_id, fields, values)
                elif ingredient_choice == "3":
                    ingredient_id = input("Enter the id of the ingredient to display: ")
                    i.read_record('ingredients', 'ingredient_id', ingredient_id)
                elif ingredient_choice == "4":
                    i.read_all_records('ingredients')
                elif ingredient_choice == "5":
                    ingredient_id = input("Enter the id of the ingredient to delete: ")
                    i.delete_record('ingredients', 'ingredient_id', ingredient_id)
                elif ingredient_choice == "6":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice")
        elif main_choice == "3":
            while True:
                category_choice = category_menu()
                c = Category("recipeDB.sqlite")
                if category_choice == "1":
                    fields, values = c.input_data()
                    c.create_record('categories', fields, values)
                elif category_choice == "2":
                    category_id = input("Enter the id of the category to update: ")
                    fields, values = c.input_data()
                    c.update_record('categories', 'category_id', category_id, fields, values)
                elif category_choice == "3":
                    category_id = input("Enter the id of the category to display: ")
                    c.read_record('categories', 'category_id', category_id)
                elif category_choice == "4":
                    c.read_all_records('categories')
                elif category_choice == "5":
                    category_id = input("Enter the id of the category to delete: ")
                    c.delete_record('categories', 'category_id', category_id)
                elif category_choice == "6":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice")
        elif main_choice == "4":
            while True:
                user_choice = user_menu()
                u = User("recipeDB.sqlite")
                if user_choice == "1":
                    fields, values = u.input_data()
                    u.create_record('users', fields, values)
                elif user_choice == "2":
                    user_id = input("Enter the id of the user to update: ")
                    fields, values = u.input_data()
                    u.update_record('users', 'user_id', user_id, fields, values)
                elif user_choice == "3":
                    user_id = input("Enter the id of the user to display: ")
                    u.read_record('users', 'user_id', user_id)
                elif user_choice == "4":
                    u.read_all_records('users')
                elif user_choice == "5":
                    user_id = input("Enter the id of the user to delete: ")
                    u.delete_record('users', 'user_id', user_id)
                elif user_choice == "6":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice")
        elif main_choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Select from the below options.")


if __name__ == "__main__":
    main()
