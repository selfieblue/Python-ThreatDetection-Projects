import datetime
import subprocess
import time

def CheckSQL():
	
	stdtime = datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')
	result = []
	#cmd = "mysql --login-path=weblogadmin mysql -e \"select distinct(thread_id) from mysql.general_log where user_host NOT LIKE '%weblogadmin%' and argument like '%logapp%' and event_time > '"+str(currtime)+"'\""
	cmd = "mysql --login-path=weblogadmin mysql -e \"select max(event_time) from mysql.general_log where user_host NOT LIKE '%weblogadmin%' and argument like '%logapp%'\""
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, errs = proc.communicate(timeout=15)
	outs = out.splitlines()
	for line in outs:
		currdt = str(line).replace("b'","")
	lastdatetime = currdt.replace("'","")
	time.sleep(2)
	
	cmd2 = "mysql --login-path=weblogadmin mysql -e \"select distinct(thread_id) from mysql.general_log where user_host NOT LIKE '%weblogadmin%' and argument like '%logapp%' and event_time > '"+str(lastdatetime)+"'\" > /home/mysqladmin/log-client/sql.output.txt; cat /home/mysqladmin/log-client/sql.output.txt"
	proc2 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
	out2, errs2 = proc2.communicate(timeout=15)
	outs2 = out2.splitlines()
	#print(cmd)
	#print(out2)
	if (str(outs2) == "b''"):
		stdtxt = "DBSERVER||mysql-server||SQL"
		loglevel = "||Normal"
		txt ="||Normal State"
		action = "||none"
		newstdtime = "||" +stdtime
		stdtxt += loglevel
		stdtxt += newstdtime
		stdtxt += txt
		stdtxt += action
		result.append(stdtxt)
	else:
		count = 0
		with open('sql.output.txt','r') as sqlresultfile:
			for line in sqlresultfile:
				stdtxt = "DBSERVER||mysql-server||SQL"
				threadid = line.strip('\n')
				#print(threadid + " count = "+ str(count))
				if (count > 0):
					#print(threadid)
					killcmd ="mysql --login-path=mysqladmin -e \"kill connection "+ str(threadid) + "\""
					killproc = subprocess.Popen(killcmd, shell=True, stdout=subprocess.PIPE)
					killout, killerrs = killproc.communicate(timeout=15)
					loglevel = "||Critical"
					txt ="||Killed connection id : "+str(threadid)
					action = "||Terminated MySQL Connection"
					newstdtime = "||" +stdtime
					stdtxt += loglevel
					stdtxt += newstdtime
					stdtxt += txt
					stdtxt += action
					result.append(stdtxt)
				count += 1
	
	return result
	
#if __name__ == "__main__":
#	CheckSQL()
