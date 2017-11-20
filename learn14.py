import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd=None, db='mysql')

cur = conn.cursor()
cur.execute("show databases;")
cur.execute("show tables;")
print(cur.fetchone())
cur.close()
conn.close()
