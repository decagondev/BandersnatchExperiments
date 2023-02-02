# Build Sprint 1: Database Operations

To begin work on this ticket, make sure you have finished:
- Getting locally setup.
- Completed the onboarding module in your course.

## Objectives

- Develop a database interface class
- Create random data
- Populate the database with at least 1000 datapoints

To see what your final output should be, navigate to `/data` on the [deployed site](https://bandersnatch.herokuapp.com/).

## Relevant Files

Access `app/data.py`, where you will add your code for this ticket. 

Stuck? Post in `labs-ds` or open a support ticket in the Hub!

## Deliverables
Submit the following in your course:

- Link to your forked repo with the added code for the landing page
- Link to a Loom video answering the prompt in the `Submit Your Deliverables` Assignment in your course


## Guidance

Once you have completed all prerequisites, you will need to create a database interface. This database interface will allow you to seed a collection with a specified number of documents, reset the collection by deleting all documents, count the number of documents in the collection, and generate a DataFrame or HTML table representation of the collection's documents. It uses the MongoClient library to connect to a MongoDB database, and the pandas library to generate a DataFrame. The database connection URL should be stored in environment variable for security.

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
