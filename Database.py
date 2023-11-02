import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_record(self, table, fields, values):
        try:
            self.cursor.execute(f"""
                INSERT INTO {table} ({', '.join(fields)})
                VALUES ({', '.join(['?' for _ in values])})
            """, values)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Record already exists: {values}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    def read_record(self, table, key, key_value):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {key} = ?", (key_value,))
        return self.cursor.fetchone()

    def update_record(self, table, key, key_value, fields, values):
        try:
            self.cursor.execute(f"""
                UPDATE {table}
                SET {', '.join([f'{field} = ?' for field in fields])}
                WHERE {key} = ?
            """, (*values, key_value))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    def delete_record(self, table, key, key_value):
        self.cursor.execute(f"DELETE FROM {table} WHERE {key} = ?", (key_value,))
        self.conn.commit()

    def reset_database(self):
        # Remove existing tables if they exist
        self.cursor.execute("""
            DROP TABLE IF EXISTS recipes;
            DROP TABLE IF EXISTS ingredients;
            DROP TABLE IF EXISTS recipe_ingredients;
            DROP TABLE IF EXISTS categories;
            DROP TABLE IF EXISTS users;
        """)

        # Create new tables
        self.cursor.execute("""
            CREATE TABLE categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT NOT NULL,
                category_description TEXT
            );

            CREATE TABLE ingredients (
                ingredient_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );

            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
            );

            CREATE TABLE recipes (
                recipe_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                instructions TEXT,
                prep_time INTEGER,
                cook_time INTEGER,
                image_url TEXT,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            );

            CREATE TABLE recipe_ingredients (
                FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
                FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),
                quantity INTEGER NOT NULL,
                unit TEXT NOT NULL,
                PRIMARY KEY(recipe_id, ingredient_id)
            );
        """)
