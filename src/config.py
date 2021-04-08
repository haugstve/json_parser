import os


def config(filename="database.ini", section="postgresql"):
    db = {}
    db["user"] = os.environ["POSTGRES_USER"]
    db["password"] = os.environ["POSTGRES_PASSWORD"]
    db["database"] = os.environ["POSTGRES_DB"]
    db["host"] = os.environ["DB_HOST"]
    print(db)
    return db
