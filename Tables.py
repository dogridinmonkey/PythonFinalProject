import Database as db
import bcrypt


class User(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

    def input_data(self):
        fields = ['username', 'password']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            value = input(f"{field}: ")
            values.append(value)
        return fields, values

    def create_user(self, username, password):
        hashed_password = self.hash_password(password)
        super().create_record('users', ['username', 'password'], [username, hashed_password])

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode('utf-8')

    def check_password(self, username, password):
        user = self.read_record('users', 'username', username)
        if user:
            hashed_password = user[2]  # assuming password is the third column
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        return False


class Recipe(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                recipe_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                instructions TEXT NOT NULL,
                prep_time TEXT,
                cook_time TEXT,
                category_id INTEGER,
                image_url TEXT,
                FOREIGN KEY (category_id) REFERENCES categories (category_id)
            )
        """)

    def input_data(self):
        fields = ['name', 'instructions', 'prep_time', 'cook_time', 'category_id', 'image_url']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            value = input(f"{field}: ")
            values.append(value)
        return fields, values


class Ingredient(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                ingredient_id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL
            )
        """)

    def input_data(self):
        fields = ['name']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            value = input(f"{field}: ")
            values.append(value)
        return fields, values


class RecipeIngredient(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
                recipe_id INTEGER NOT NULL,
                ingredient_id INTEGER NOT NULL,
                quantity TEXT NOT NULL,
                measurement TEXT,
                PRIMARY KEY (recipe_id, ingredient_id),
                FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id)
            )
        """)

    def input_data(self):
        fields = ['recipe_id', 'ingredient_id', 'quantity', 'measurement']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            value = input(f"{field}: ")
            values.append(value)
        return fields, values


class Category(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL
            )
        """)

    def input_data(self):
        fields = ['name']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            value = input(f"{field}: ")
            values.append(value)
        return fields, values
