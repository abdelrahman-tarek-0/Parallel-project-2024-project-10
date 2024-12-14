import time
import sqlite3

class DataFetcher:
    @staticmethod
    def fetch(db = "db.sqlite3", fake_delay=2, num_of_posts=5):
        time.sleep(fake_delay)

        con = sqlite3.connect(f"./databases/{db}")
        cur = con.cursor()
        data_list = [a for a in cur.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT ?", (num_of_posts,))]

        data = []

        for d in data_list:
            data.append({
                "id": d[0],
                "name": d[1],
                "avatar": d[2],
                "quote": d[3],
                "source": db
            })

        con.close()

        return data
