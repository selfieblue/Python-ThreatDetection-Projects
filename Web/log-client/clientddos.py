import datetime
import subprocess
import time

def CheckDDOS():
	stdtime = datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')
	result = []
	cmd = "netstat -atun | awk '{print $5}' | cut -d: -f1 | sed -e '/^$/d' |sort | uniq -c | sort -n"
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out, errs = proc.communicate(timeout=15)
	outs = out.splitlines()
	for line in outs:
		rawline = str(line).replace("b'","")
		currline = rawline.replace("'","").strip()
		linespit = currline.split(' ')
		numcon = linespit[0]
		ip = linespit[1]
		if(ip == "Address" or ip == "and"):
			pass
			stdtxt = "WEBSERVER||webserver1||DDOS"
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
			#print(numcon+" "+ip)
			if(int(numcon) >=10):
				stdtxt = "WEBSERVER||webserver1||DDOS"
				loglevel = "||Critical"
				txt ="||Detected IP : "+ ip + " is attacking by DDoS"
				action = "||Report"
				newstdtime = "||" +stdtime
				stdtxt += loglevel
				stdtxt += newstdtime
				stdtxt += txt
				stdtxt += action
				result.append(stdtxt)
				
	return result

#if __name__ == "__main__":
#	CheckDDOS()
