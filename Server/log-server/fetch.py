import MySQLdb
import datetime
conn = MySQLdb.connect(host= "mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
sqlcursor = conn.cursor()
sqlcursor.execute("SELECT logrole,logserver,logtype,loglevel,CAST(logdatetime AS CHAR),logdetail,logaction,logread FROM logapp_logtable")
row = sqlcursor.fetchall()
for data in row:
	print(str(data))
conn.close()
