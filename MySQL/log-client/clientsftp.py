import subprocess
import datetime
import time

def CheckSFTP():
	result = []
	txt = "||Normal State"
	loglevel = "||Normal"
	action = "||none"
	with open('ftp-last-query-date','r') as f:
		ltime = f.read()
		lastdatetime = ltime.strip('\n')
	lastquerydatetime = constrtt = datetime.datetime.strptime(lastdatetime, '%b %d %Y %H:%M:%S')
	#print(lastdatetime)
	time.sleep(1)
	cmd = "tail -100 /var/log/auth.log | grep -i 'sftp-server'"
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, errs = proc.communicate(timeout=15)
	outs = out.splitlines()
	check = 0
	for line in outs:
		fullretrun = "DBSERVER||mysql-server||SFTP"
		rawlog = str(line)
		rawsplit = rawlog.split(' ')
		curryear = datetime.datetime.now().year
		rawdatetime = rawsplit[0].replace("b'","")+" "+rawsplit[1]+" "+str(curryear)+" "+rawsplit[2]
		#print("---->"+rawdatetime)
		logcurrdatetime = datetime.datetime.strptime(rawdatetime, '%b %d %Y %H:%M:%S')
		
		if (lastquerydatetime <= logcurrdatetime):
			if(rawlog.find("session opened") >= 0):
				check = 1
				logip = rawsplit[12]
				user = rawsplit[10]
				#print(logip)
				loglevel = "||Normal"
				txt = "||SFTP Login user : "+ user +" from ip : "+logip
				action = "||none"
				checkbl = 0
				fullretrun += loglevel
				timesend = "||" + rawdatetime
				fullretrun += timesend
				fullretrun += txt
				fullretrun += action
				print(fullretrun)
				result.append(fullretrun)
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
					fullretrun += loglevel
					timesend = "||" + rawdatetime
					fullretrun += timesend
					fullretrun += txt
					fullretrun += action
					print(fullretrun)
					result.append(fullretrun)
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
			
			if(rawlog.find("flags READ") >= 0 and check == 1):
				filename = rawsplit[6]
				loglevel = "||Normal"
				txt = "||User : "+ user +" from ip : "+logip +" Copied file name : " + filename
				action = "||none"
				fullretrun += loglevel
				timesend = "||" + rawdatetime
				fullretrun += timesend
				fullretrun += txt
				fullretrun += action
				print(fullretrun)
				result.append(fullretrun)
				
			if(rawlog.find("flags WRITE") >= 0 and check == 1):
				filename = rawsplit[6]
				loglevel = "||Normal"
				txt = "||User : "+ user +" from ip : "+logip +" Pasted file name : " + filename +" to your system"
				action = "||none"
				fullretrun += loglevel
				timesend = "||" + rawdatetime
				fullretrun += timesend
				fullretrun += txt
				fullretrun += action
				print(fullretrun)
				result.append(fullretrun)
			
			if(rawlog.find("session closed") >= 0 and check == 1):
				loglevel = "||Normal"
				txt = "||Close SFTP session for user : "+ user +" from ip : "+logip
				action = "||none"
				fullretrun += loglevel
				timesend = "||" + rawdatetime
				fullretrun += timesend
				fullretrun += txt
				fullretrun += action
				print(fullretrun)
				result.append(fullretrun)
				
				with open('ftp-last-query-date','w') as fw:
					fw.write(rawdatetime)
				
	return result
	
#if __name__ == "__main__":
#	CheckSFTP()
