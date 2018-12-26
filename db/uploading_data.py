import MySQLdb
from connect import db


def getUploadData(table_name):
    cursor = db.cursor()

    sql = """SELECT * FROM %s WHERE uploaded = 0""" % table_name

    try:
        cursor.execute(sql)

        # cursor.description gives a tuple of tuples where [0] for each is the column name.
        field_names = [i[0] for i in cursor.description]

        dataArray = []

        for row in cursor:
            data = {}
            for field_index, field_name in enumerate(field_names):
                data[field_name] = row[field_index]

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret


def markRowsAsUploaded(table_name):
    cursor = db.cursor()

    sql = """UPDATE %s SET uploaded = 1""" % table_name

    try:
        cursor.execute(sql)
        db.commit()
        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()
        ret = False

    return ret