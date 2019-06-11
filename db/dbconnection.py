import mysql.connector
import json

conn = mysql.connector.connect(host='192.168.22.58',
                               database='device_statistics',
                               user='root',
                               password='gaian')


def get_connection():
    conn.connect()
    return conn
