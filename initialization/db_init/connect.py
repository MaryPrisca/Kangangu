import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "", "kangangu" )
db.autocommit(True)
