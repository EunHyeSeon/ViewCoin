import pymysql
import pymysql.cursors
 
def getConnect():
    conn = pymysql.connect(host='localhost',
    port=port_num, db='dbname', user='username', password='password', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    return conn
