import mysql.connector
import json

json_data = {"app_id": " ",
             "app_name": "my_app",
             "app_version": "22",
             "app_size": "32",
             "package_name": "android"}
print(type(json_data))
conn = mysql.connector.connect(host='192.168.22.58',
                               database='device_statistics',
                               user='root',
                               password='gaian')

if conn.is_connected():
    print('Connected to MySQL database')

mycursor = conn.cursor()

# query="insert into app_table('app_id','app_name', 'app_version', 'app_size', 'package_name') VALUES (%d,%s,%d,%d,%s);"
# query=("insert into app_table" "(app_id, app_name, app_version, app_size, package_name)" "VALUES (%d,%s,%d,%d,%s)")

# for i in json_data:
#   mycursor.execute(query,i)
query = 'insert into app_table VALUES (%s,%s,%s,%s,%s);'
print(json.dumps(json_data))
jsondump = json.dumps(json_data)
json_format = json.loads(jsondump)

# mycursor.execute(insert,json.dumps(json_data))
mycursor.execute(query,
                 (
                str(json_format['app_id']), str(json_format['app_name']),
                str(json_format['app_version']), str(json_format['app_size']),
                str(json_format['package_name'])
                 )
                 )

print("1 record inserted, ID:", mycursor.lastrowid)
conn.commit()
mycursor.close()
conn.close()
