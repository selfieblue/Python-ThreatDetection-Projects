import subprocess
import datetime

def CheckAuth():
	result = []
	txt = "||Normal State"
	loglevel = "||Normal"
	action = "||none"
	with open('last-query-date','r') as f:
		ltime = f.read()
		lastdatetime = ltime.strip('\n')
	lastquerydatetime = constrtt = datetime.datetime.strptime(lastdatetime, '%b %d %Y %H:%M:%S')	
	cmd = "tail -100 /var/log/auth.log | grep -i 'from'"
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, errs = proc.communicate(timeout=15)
	outs = out.splitlines()
	for line in outs:
		fullretrun ="WEBSERVER||webserver1||SSH"
		rawlog = str(line)
		rawsplit = rawlog.split(' ')
		curryear = datetime.datetime.now().year
		rawdatetime = rawsplit[0].replace("b'","")+" "+rawsplit[1]+" "+str(curryear)+" "+rawsplit[2]
		#print("---->"+rawcontent)
		logcurrdatetime = datetime.datetime.strptime(rawdatetime, '%b %d %Y %H:%M:%S')
		if (lastquerydatetime < logcurrdatetime):
			#print(rawlog)
			action = "||none"
			splitcontent = rawlog.split(' ')
			if (rawlog.find("Failed password") >= 0):
				if (rawlog.find("invalid") >= 0):
					loglevel = "||Suspicious"
					txt = "||Invalid user try to login this system with username : " + rawsplit[10] +" from IP: " + rawsplit[12]
					action = "||none"
					#print(txt)
					
				if (rawlog.find("message repeated") >= 0):
					loglevel = "||Suspicious"
					txt = "||User : " + rawsplit[13] +" try to login system "+ rawsplit[7]+ " times with invalid password from IP: " + rawsplit[15]
					action = "||none"
					#print(txt)
					
			if(rawlog.find("Accepted password") >= 0  or rawlog.find("Accepted publickey") >= 0):
				logip = rawsplit[10]
				#print(logip)
				loglevel = "||Normal"
				txt = "||SSH Login from ip : "+logip
				action = "||none"
				checkbl = 0
				with open('blacklist.ips','r') as fr:
					for line in fr:
						ip = line.strip('\n')
						if (ip == logip):
							checkbl = 1
							
				if (checkbl == 1):
					checksession = "last | grep '"+logip+"' | grep 'still logged in'"
					loglevel = "||Critical"
					txt = "||Blacklist IP try to access system : "+logip
					action = "||Terminated session form ip : "+logip
					#print(checksession)
					procses = subprocess.Popen(checksession, shell=True, stdout=subprocess.PIPE)
					outses, errsses = procses.communicate(timeout=15)
					if (str(out) != "b''"):
						action = "||Terminated SSH Session"
						sessionsplit = outses.splitlines()
						for xline in sessionsplit:
							rawsession = str(xline)
							sessioninfo = rawsession.split(' ')
							sesid = sessioninfo[1]
							processinfo = "ps -aux | grep ssh | grep "+sesid
							#print(processinfo)
							procinfo = subprocess.Popen(processinfo, shell=True, stdout=subprocess.PIPE)
							outinfo, errsinfo = procinfo.communicate(timeout=15)
							processsplit = outinfo.splitlines()
							count = 0
							for x in processsplit:
								count += 1
								if (count == 1):
									temp = str(x)
									#print(temp)
									procid = temp.split('  ')
									killcmd = "sudo kill -9 "+ procid[1].strip()
									#print(killcmd)
									killprocses = subprocess.Popen(killcmd, shell=True, stdout=subprocess.PIPE)
									#print("Killed SSH session ID : "+ procid[1])
							
		fullretrun += loglevel
		timesend = "||" + rawdatetime
		fullretrun += timesend
		fullretrun += txt
		fullretrun += action
		#print(fullretrun)
		result.append(fullretrun)
		
	with open('last-query-date','w') as fw:
		fw.write(rawdatetime)
		
	return result
	
#if __name__ == "__main__":
#		CheckAuth()
