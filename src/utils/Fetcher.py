import time
import random

from utils.Storage import InMemorySharedStorage
import sqlite3

db = "db.sqlite3"


def get_random_data():
    con = sqlite3.connect(db)
    cur = con.cursor()
    data_list = [a for a in cur.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT 5")]

    data = []

    for d in data_list:
        data.append({
            "id": d[0],
            "name": d[1],
            "avatar": d[2],
            "quote": d[3],
        })

    con.close()

    return data
  

class DataFetcher:
    @staticmethod
    def fetch(source, onLoading, onFetched, fake_delay=2):
        onLoading(source, True)
        time.sleep(fake_delay)
    
        InMemorySharedStorage.save(source, get_random_data())
        
        onLoading(source, False)
        onFetched(source)
