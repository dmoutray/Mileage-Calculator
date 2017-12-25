import pymysql

class DBConfig():
    connection = pymysql.connect(host='localhost',
                                  user='david',
                                  password='4security',
                                  db='fuel_calculator',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

