import socket
import MySQLdb
import datetime
def Main():
	host = "dockerserver"
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print("Server Started, Listenning on Port : ", str(port))
	conn = MySQLdb.connect(host="mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
	sqlcursor = conn.cursor()
	
	while True:
		data, addr = s.recvfrom(1024)
		newdata = data.decode(encoding='UTF-8')
		print("message from : "+str(addr)+" content : "+ str(newdata))
		contentsplit = newdata.split('||')
		logtime = datetime.datetime.strptime(contentsplit[4], '%b %d %Y %H:%M:%S')
		#Table : logapp_logtable
		strlog = "insert into logapp_logtable (logrole,logserver,logtype,loglevel,logdatetime,logdetail,logaction,logread) values"
		strlog += "('"+contentsplit[0]+"','"+contentsplit[1]+"','"+contentsplit[2]+"','"+contentsplit[3]+"','"+str(logtime)+"','"+contentsplit[5].replace("'","")+"','"+contentsplit[6]+"','N')"
		#print(strlog)
		try:
			sqlcursor.execute(strlog) 
			#print("Here")
			conn.commit()
		except:
			conn.rollback()
		
	s.close()
	conn.close()
	
if __name__ == "__main__":
	Main()
