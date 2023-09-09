# Create an sqlite3 database by reading data from a csv
import hushhushDB_V1
import pandas as pd

df = pd.read_csv("github_final_dataset.csv")

# print(df)
# hushhushDB.create_table()
# hushhushDB.import_data(df)
query = "SELECT name, followers FROM candidates_table WHERE followers > 2000 ORDER BY followers DESC"
rows = hushhushDB_V1.pass_query(query)
for row in rows:
    print(row)
