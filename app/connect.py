from typing import Dict
import psycopg2
import os
from transform_input import Target


class DataBase:
    conn = None
    table_name: str

    def __init__(self, table_name) -> None:
        self.table_name = table_name
        self.connect()
        self.create_table()

    def create_table(self) -> None:
        if not self.conn:
            self.connect()
        with self.conn.cursor() as cur:
            command = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id serial NOT NULL PRIMARY KEY, info json NOT NULL);"
            print(command)
            cur.execute(command)

    def add_json_to_table(self, payload: Target) -> None:
        if not self.conn:
            self.conn = self.connect()
        with self.conn.cursor() as cur:
            command = (
                f"INSERT INTO {self.table_name} (info) VALUES('{payload.to_json()}');"
            )
            cur.execute(command)

    def read_all_entries(self) -> None:
        if not self.conn:
            self.connect()
        with self.conn.cursor() as cur:
            command = f"SELECT info from {self.table_name};"
            cur.execute(command)
            result = cur.fetchall()
        return result

    def connect(self):
        if self.conn is not None:
            self.conn.close()
        try:
            params = self._get_config_()
            self.conn = psycopg2.connect(**params)
            self.conn.autocommit = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def _get_config_(self) -> Dict:
        config = {}
        config["user"] = os.environ["POSTGRES_USER"]
        config["password"] = os.environ["POSTGRES_PASSWORD"]
        config["database"] = os.environ["POSTGRES_DB"]
        config["host"] = os.environ["DB_HOST"]
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
