import socket
import clientssh
import clientddos
import clientsftp
import time
def Main():
	host = "webserver1"
	port = 5001
	server=("192.168.10.144",5000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	
	while True:
	
		arrclient = clientssh.CheckAuth()
		for message1 in arrclient:
			temp1 = message1.split('||')
			if (temp1[5] != "Normal State"):
				print(message1)
				sendmessage = bytes(message1, encoding='UTF-8')
				s.sendto(sendmessage,server)
				
		ddosclient = clientddos.CheckDDOS()
		for message2 in ddosclient:
			temp2 = message2.split('||')
			if (temp2[5] != "Normal State"):
				print(message2)
				sendmessage = bytes(message2, encoding='UTF-8')
				s.sendto(sendmessage,server)
		
		sftpclient = clientsftp.CheckSFTP()
		for message3 in sftpclient:
			temp3 = message3.split('||')
			if (temp3[5] != "Normal State"):
				print(message3)
				sendmessage = bytes(message3, encoding='UTF-8')
				s.sendto(sendmessage,server)
			
		time.sleep(1)
	s.close()
	
if __name__ == "__main__":
	Main()
