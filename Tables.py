import Database as db
import bcrypt


class User(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username VARCHAR UNIQUE NOT NULL,
                password VARCHAR NOT NULL,
                email VARCHAR UNIQUE NOT NULL
            )
        """)

    def input_data(self):
        fields = ['username', 'password', 'email']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            while True:
                value = input(f"{field.title()}: ")
                if field == 'username':
                    self.cursor.execute(f"SELECT * FROM users WHERE username = ?", (value,))
                    record = self.cursor.fetchone()
                    if record is not None:
                        print("A user with this username already exists. Please enter a unique username.")
                        continue
                values.append(value)
                break
        return fields, values

    def create_user(self, username, password, email):
        hashed_password = self.hash_password(password)
        super().create_record('users', ['username', 'password'], [username, hashed_password, email])

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
                name VARCHAR UNIQUE NOT NULL,
                instructions VARCHAR,
                prep_time INTEGER,
                cook_time INTEGER,
                image_url VARCHAR,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (category_id)
            )
        """)

    def input_data(self):
        fields = ['name', 'instructions', 'prep_time', 'cook_time', 'image_url', 'category_id']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            while True:
                value = input(f"{field.title()}: ")
                if field == 'name':
                    self.cursor.execute(f"SELECT * FROM recipes WHERE name = ?", (value,))
                    record = self.cursor.fetchone()
                    if record is not None:
                        print("A recipe with this name already exists. Please enter a unique name.")
                        continue
                values.append(value)
                break
        return fields, values


class Ingredient(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                ingredient_id INTEGER PRIMARY KEY,
                name VARCHAR UNIQUE NOT NULL
            )
        """)

    def input_data(self):
        fields = ['name']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            while True:
                value = input(f"{field.title()}: ")
                if field == 'name':
                    self.cursor.execute(f"SELECT * FROM your_table WHERE name = ?", (value,))
                    record = self.cursor.fetchone()
                    if record is not None:
                        print("A record with this name already exists. Please enter a unique name.")
                        continue
                values.append(value)
                break
        return fields, values


class RecipeIngredient(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
                recipe_id INTEGER NOT NULL,
                ingredient_id INTEGER NOT NULL,
                quantity VARCHAR NOT NULL,
                measurement VARCHAR,
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
            value = input(f"{field.title()}: ")
            values.append(value)
        return fields, values


class Category(db.Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY,
                category_name VARCHAR UNIQUE NOT NULL
            )
        """)

    def input_data(self):
        fields = ['name']
        values = []
        print("Please enter the following details: ")
        for field in fields:
            while True:
                value = input(f"{field.title()}: ")
                if field == 'name':
                    self.cursor.execute(f"SELECT * FROM your_table WHERE name = ?", (value,))
                    record = self.cursor.fetchone()
                    if record is not None:
                        print("A record with this name already exists. Please enter a unique name.")
                        continue
                values.append(value)
                break
        return fields, values
