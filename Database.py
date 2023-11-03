import sqlite3
import csv


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def populate_from_csv(self, table, csv_file):
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            fields = next(reader)  # Get the column names from the first row
            for row in reader:
                # Only include values for which there is a corresponding field
                values = [value for field, value in zip(fields, row) if field]
                self.create_record(table, fields, values)

    def create_record(self, table, fields, values):
        sql = f"""
            INSERT INTO {table} ({', '.join(fields)})
            VALUES ({', '.join(['?' for _ in values])})
        """
        # print(f"SQL: {sql}")
        # print(f"Values: {values}")
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"\nRecord added successfully: {values[0]}")
        except sqlite3.IntegrityError:
            print(f"\nRecord already exists: {values[0]}")
        except sqlite3.Error as e:
            print(f"\nAn error occurred: {e.args[0]}")

    def read_record(self, table, key, key_value):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {key} = ?", (key_value,))
        record = self.cursor.fetchone()
        if record is not None:
            print("\n")  # new line before record displays
            field_names = [description[0] for description in self.cursor.description]
            friendly_names = {field_name: field_name.replace('_', ' ').title() for field_name in field_names}
            for field_name, item in zip(field_names, record):
                print(f"{friendly_names.get(field_name, field_name)}: {item}")
        else:
            print(f"\nNo record found for {key_value}")

    def read_all_records(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        records = self.cursor.fetchall()
        if records:
            print("\n")  # new line before records display
            field_names = [description[0] for description in self.cursor.description]
            friendly_names = {field_name: field_name.replace('_', ' ').title() for field_name in field_names}
            for record in records:
                for field_name, item in zip(field_names, record):
                    print(f"{friendly_names.get(field_name, field_name)}: {item}")
                print("\n")  # new line between records
        else:
            print("\nNo records found.")

    def update_record(self, table, key, key_value, fields, values):
        try:
            self.cursor.execute(f"""
                UPDATE {table}
                SET {', '.join([f'{field} = ?' for field in fields])}
                WHERE {key} = ?
            """, (*values, key_value))
            self.conn.commit()
            print(f"Record updated successfully: {values[0]}")
        except sqlite3.Error as e:
            print(f"\nAn error occurred: {e.args[0]}")

    def delete_record(self, table, key, key_value):
        self.cursor.execute(f"DELETE FROM {table} WHERE {key} = ?", (key_value,))
        self.conn.commit()
        print(f"\nRecord deleted successfully: {key_value[0]}")

    def reset_database(self):
        # Remove existing tables if they exist
        tables_to_drop = ["recipes", "ingredients", "recipe_ingredients", "categories", "users"]
        for table in tables_to_drop:
            self.cursor.execute(f"DROP TABLE IF EXISTS {table};")

        # Create new empty tables
        self.cursor.execute("""
            CREATE TABLE categories (
                category_id INTEGER PRIMARY KEY,
                category_name VARCHAR UNIQUE NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE ingredients (
                ingredient_id INTEGER PRIMARY KEY,
                name VARCHAR UNIQUE NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                username VARCHAR UNIQUE NOT NULL,
                password VARCHAR NOT NULL,
                email VARCHAR UNIQUE NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE recipes (
                recipe_id INTEGER PRIMARY KEY,
                name VARCHAR UNIQUE NOT NULL,
                instructions VARCHAR,
                prep_time INTEGER,
                cook_time INTEGER,
                image_url VARCHAR,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES categories(category_id)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE recipe_ingredients (
                recipe_id INTEGER,
                ingredient_id INTEGER,
                quantity INTEGER NOT NULL,
                unit TEXT NOT NULL,
                PRIMARY KEY(recipe_id, ingredient_id),
                FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
                FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id)
            );
        """)

        self.conn.commit()
        print("\nDatabase reset successfully.")

