import test

"""
# Database driver to be used (currently set to MySQL)
db_driver = "mysql"
db_user = "hoi4intel"
db_password = "."
db_name = "hoi4intel"
db_host = "host.igportals.tk"

"""
# Uncomment the following block to use MongoDB instead of MySQL
# Database driver to be used (currently set to MongoDB)
db_driver = "mongodb"
db_user = "hoi4intel"
db_password = "."
db_name = "hoi4intel"
db_host = "hoi4intel.ssaonbs.mongodb.net"

db = test.database(db_driver, db_user, db_password, db_name, db_host)

query = db.select("players", ({"rating": 0.5}))


#query = db.select_all_order("players", "id", "desc")

for i in query:
    print(i)
