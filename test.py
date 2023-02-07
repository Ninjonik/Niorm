import main

"""
# Database driver to be used (currently set to MySQL)
db_driver = "mysql"
db_user = "hoi4intel"
db_password = "7tN7i3sSxXuYSFk"
db_name = "hoi4intel"
db_host = "host.igportals.tk"

"""
# Uncomment the following block to use MongoDB instead of MySQL
# Database driver to be used (currently set to MongoDB)
db_driver = "mongodb"
db_user = "hoi4intel"
db_password = "X8XQ9PNFAsF0CcMG"
db_name = "hoi4intel"
db_host = "hoi4intel.ssaonbs.mongodb.net"


db = main.database(db_driver, db_user, db_password, db_name, db_host)

# EXAMPLE USE CASES

# INSERT
# query = db.insert("players", {"discord_id": 894589})
# SELECT ALL
# query = db.select_all("players")
# for i in query:
#     print(i["rating"])
# SELECT ALL ORDER
# query = db.select_all_order("players", "created_at", "desc")
# for i in query:
#     print(i["created_at"])
# SELECT WHERE
# query = db.select("players", {"rating": 48})
# for i in query:
#     print(i["rating"])
# DELETE
# query = db.delete("players", {"rating": 1})
# UPDATE
# query = db.update("players", {"rating": 0.45}, {"rating": 0.5})

