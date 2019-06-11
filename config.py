import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='192.168.22.58',
                                       database='device_statistics',
                                       user='root',
                                       password='gaian')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


