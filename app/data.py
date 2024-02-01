from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self):
        load_dotenv()
        client = MongoClient(getenv("DB_URL"))
        db = client["Monster_Database"]
        self.collection = db["Monsters"]

    def seed(self, amount):
        for _ in range(amount):
            monster = Monster().to_dict()
            self.collection.insert_one(monster)

    def reset(self):
        self.collection.delete_many({})

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        cursor = self.collection.find({}, {"_id": 0})
        df = DataFrame(cursor)
        return df

    def html_table(self) -> str:
        df = self.dataframe()
        table = df.to_html(index=True)
        return table

if __name__ == '__main__':
    db = Database()
    # db.reset()  # resets seeded number
    db.seed(1000)
    print(db.count())
    print(list(db.collection.find({}, {"_id": 0})))