import pymongo
import datetime
from bson.objectid import ObjectId
import mysql.connector

db_driver = 0
db_user = 0
db_password = 0
db_name = 0
db_host = 0

# Function to return the appropriate database object based on the selected driver
def database(dbdriver, dbuser, dbpassword, dbname, dbhost):
    global db_driver
    global db_user
    global db_password
    global db_name
    global db_host
    db_driver = dbdriver
    db_user = dbuser
    db_password = dbpassword
    db_name = dbname
    db_host = dbhost
    if dbdriver == "mysql":
        return NiormMySQL()
    elif dbdriver == "mongodb":
        return NiormMongoDB()


# Converts a dictionary of data into a string suitable for use in a SQL statement
def dict_to_values_string(data):
    keys = ", ".join(data.keys())
    values = ", ".join(str(val) for val in data.values())
    return f"({keys}) VALUES ({values})"

def dict_to_sql_where(d):
    return " AND ".join("{}='{}'".format(k, v) for k, v in d.items())


# Class for connecting to a MySQL database using the niorm library
class NiormMySQL:
    def __init__(self):
        # Connect to the database using the specified credentials
        connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
        )
        self.connection = connection
        self.cursor = connection.cursor()

    # Insert a new row into the specified table with the given data
    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, columns, placeholders)
        self.cursor.execute(sql, tuple(data.values()))
        self.connection.commit()
        return True

    # Retrieve all rows from the specified table
    def select_all(self, table):
        self.cursor.execute("SELECT * FROM %s" % table)
        return self.cursor.fetchall()

    # Retrieve all rows from the specified table and order them based on the given column
    def select_all_order(self, table, column, order):
        self.cursor.execute("SELECT * FROM %s ORDER BY %s %s" % (table, column, order))
        return self.cursor.fetchall()

    # Retrieve all rows from the specified table that match the given conditions
    def select(self, table, data):
        data = dict_to_sql_where(data)
        self.cursor.execute("SELECT * FROM %s WHERE %s" % (table, data))
        return self.cursor.fetchall()
    
    # Delete all rows from the specified table that match the given conditions
    def delete(self, table, data):
        data = dict_to_sql_where(data)
        self.cursor.execute("DELETE FROM %s WHERE %s" % (table, data))
        return True

    def update(self, table, where, data):
        new_values = {"$set": data}
        self.db[table].update_one(where, new_values)
        return True


class NiormMongoDB:

    def __init__(self):
        client = pymongo.MongoClient(
            f"mongodb+srv://{db_user}:{db_password}@{db_host}/?retryWrites=true&w=majority")
        dblist = client.list_database_names()
        if db_name in dblist:
            self.db = client[db_name]
            print("Successfully connected to MongoDB.")
        else:
            print("Error: Failed to connect to MongoDB.")
            quit()

    def insert(self, table, data):
        """Inserts a single document into the specified table in MongoDB."""
        return self.db[table].insert_one(data)

    def select_all(self, table):
        """Returns all documents from the specified table in MongoDB."""
        return self.db[table].find()

    def select_all_order(self, table, column, order):
        """Returns all documents from the specified table in MongoDB, ordered by the specified column and order."""
        return self.db[table].find().sort(column, -1 if order.lower() == "desc" else 1)

    def select(self, table, data):
        """Returns documents that match the specified filter from the specified table in MongoDB."""
        return self.db[table].find(data)

    def delete(self, table, data):
        """Deletes a single document that matches the specified filter from the specified table in MongoDB."""
        self.db[table].delete_one(data)
        return True

    def update(self, table, where, data):
        """Updates a single document that matches the specified filter with the specified data in the specified table
        in MongoDB. """
        new_values = {"$set": data}
        self.db[table].update_one(where, new_values)
        return True
