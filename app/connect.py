from typing import Dict
import psycopg2
import os
from transform_input import Target


class DataBase:
    conn = None
    table_name: str

    def __init__(self, table_name) -> None:
        self.table_name = table_name
        self.conn = self.connect()
        self.create_table()

    def create_table(self) -> None:
        if not self.conn:
            self.conn = self.connect()
        cur = self.conn.cursor()
        command = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id serial NOT NULL PRIMARY KEY, info json NOT NULL);"
        print(command)
        cur.execute(command)
        cur.close()

    def add_json_to_table(self, payload: Target) -> None:
        if not self.conn:
            self.conn = self.connect()
        cur = self.conn.cursor()
        command = f"INSERT INTO {self.table_name} (info) VALUES('{payload.to_json()}');"
        print(f"Running command: {command}")
        cur.execute(command)
        cur.close()

    def read_all_entries(self) -> None:
        if not self.conn:
            self.conn = self.connect()
        cur = self.conn.cursor()
        command = f"SELECT info from {self.table_name};"
        print(f"Running command: {command}")
        cur.execute(command)
        result = cur.fetchall()
        print(f"Result from query: {result}")
        cur.close()
        return result

    def connect(self):
        """ Connect to the PostgreSQL database server """
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed.")
        try:
            params = self._get_config_()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            conn.autocommit = True
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def _get_config_(self) -> Dict:
        config = {}
        config["user"] = os.environ["POSTGRES_USER"]
        config["password"] = os.environ["POSTGRES_PASSWORD"]
        config["database"] = os.environ["POSTGRES_DB"]
        config["host"] = os.environ["DB_HOST"]
        print(f"Returning database info {config}")
        return config

    def test_connection(self):
        if not self.conn:
            self.conn = self.connect()
        cur = self.conn.cursor()
        print("PostgreSQL database version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()

    # conn.autocommit = True


# def test_connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         params = config()

#         print("Connecting to the PostgreSQL database...")
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()

#         print("PostgreSQL database version:")
#         cur.execute("SELECT version()")

#         db_version = cur.fetchone()
#         print(db_version)

#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print("Database connection closed.")
