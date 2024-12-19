import sqlite3

class Database:
    def __init__(self, path:str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS survey_results(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                instagram_username TEXT NOT NULL,
                food_rating INTEGER NOT NULL,
                cleanliness_rating INTEGER NOT NULL,
                visit_date TEXT NOT NULL,
            )
            """)
            # conn.execute("""
            #     CREATE TABLE IF NOT EXISTS meals(
            #     id INTEGER PRIMARY KEY AUTOINCREMENT,
            #     name TEXT NOT NULL,
            #     price INTEGER NOT NULL,
            #     genre TEXT
            #     )
            # """)
            conn.commit()

    def save_survey(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO survey_results (name, instagram_username,food_rating, cleanliness_rating, visit_date )
                VALUES (?,?,?,?,?,?)
                """,
                (data['name'], data['instagram_username'],data['food_rating'], data['cleanliness_rating'],data['visit_date'])
            )
