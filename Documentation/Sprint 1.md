# Sprint 1: Database Operations
- A. Implement a Database Interface
- B. Generate Random Data
- C. Populate the Database

This database interface will allow you to seed a collection with a specified number of documents, reset the collection by deleting all documents, count the number of documents in the collection, and generate a DataFrame or HTML table representation of the collection's documents. It uses the MongoClient library to connect to a MongoDB database, and the pandas library to generate a DataFrame. The database connection URL should be stored in environment variable for security.

## A. Implement a Database Interface
- Starter File: `app/data.py`
- Suggested Database: MongoDB

### 1. Database Setup
- [ ] Signup for a MongoDB account: [MongoDB](https://account.mongodb.com)
- [ ] Create a "Shared Cluster" (free tier)
- [ ] Add your IP address to the allowed locales list
- [ ] Copy the connection string into a `.env` file
    - `DB_URL=mongodb+srv://<username>:<password>@<cluster>.<project_id>.mongodb.net`

### 2. Functionality
- [ ] The seed() function correctly inserts the specified number of documents into the collection.
- [ ] The reset() function correctly deletes all documents from the collection.
- [ ] The count() function correctly returns the number of documents in the collection.
- [ ] The dataframe() function correctly returns a DataFrame containing all documents in the collection.
- [ ] The html_table() function correctly returns an HTML table representation of the DataFrame, or None if the collection is empty.

### 3. Security
- [ ] The database URL is stored in an environment variable and is not hardcoded into the component.
- [ ] The TLS certificate authority file is properly configured and used to establish a secure connection to the database.

### 4. Documentation & Style
- [ ] The code includes docstrings explaining the purpose and behavior of each component.
- [ ] The code includes no extraneous comments and no inline print statements.
- [ ] The code follows PEP style guide.

### Required Methods
- `.seed(amount)`
  - Populates the database collection with random monster data
- `.reset()`
  - Delete all data in the database collection
- `.count() -> int`
  - Returns the number of records in the database collection
- `.dataframe() -> DataBase`
  - Returns the collection in the form of a pandas DataFrame
- `.html_table() -> str`
  - Returns the collection in the form of an HTML table

#### Example Database Interface: CRUD Operations
```python
from os import getenv
from typing import Dict, Iterable, Iterator
from random import randrange

from pandas import DataFrame
from pymongo import MongoClient
from dotenv import load_dotenv
from certifi import where


class MongoDB:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]
    
    def __init__(self, collection: str):
        self.collection = self.database[collection]

    def create_one(self, record: Dict) -> bool:
        return self.collection.insert_one(record).acknowledged

    def read_one(self, query: Dict) -> Dict:
        return self.collection.find_one(query, {"_id": False})

    def update_one(self, query: Dict, update: Dict) -> bool:
        return self.collection.update_one(query, {"$set": update}).acknowledged

    def delete_one(self, query: Dict) -> bool:
        return self.collection.delete_one(query).acknowledged

    def create_many(self, records: Iterable[Dict]) -> bool:
        return self.collection.insert_many(records).acknowledged

    def read_many(self, query: Dict) -> Iterator[Dict]:
        return self.collection.find(query, {"_id": False})

    def update_many(self, query: Dict, update: Dict) -> bool:
        return self.collection.update_many(query, {"$set": update}).acknowledged

    def delete_many(self, query: Dict) -> bool:
        return self.collection.delete_many(query).acknowledged


if __name__ == '__main__':
    db = MongoDB("Collection")
    db.create_many({"Value": randrange(1, 100)} for _ in range(10))
    print(DataFrame(db.read_many({})))

```

---

### B. Generate Random Data
- [ ] Use the MonsterLab library to generate random data
- [ ] Store the generated data in a csv file
- [ ] Practice statistical analysis in a notebook
- [ ] What can we learn about the data?

```python
from pandas import DataFrame
from MonsterLab import Monster


df = DataFrame(Monster().to_dict() for _ in range(10))
print(df)

```

---

### C. Populate the Database
- [ ] Use the database interface `seed(amount)` method to populate the database
- [ ] Varify the number of rows created with the `count()` method
- [ ] Get ready for the next Sprint - create a notebook for data visualization
