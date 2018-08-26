import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "", "school_management_system")
# db.ping(True)
db.autocommit(True)
