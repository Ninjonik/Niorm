import main

db = main.NiormMongoDB()

query = db.select("customers", ({"name": "zecpsa"}))


#query = db.select_all_order("players", "id", "desc")

for i in query:
    print(i)

