import MySQLdb
import datetime

from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
   return render_to_response('index.html', context_instance=RequestContext(request))

def fetch_web(request):
	all_result ="<table class='hovertable'>"
	all_result += "<tr><th>Server Name </th><th>Log Time</th><th>Current Status</th><th>Action</th></tr>"
	conn = MySQLdb.connect(host= "mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
	sqlcursor = conn.cursor()
	sqlcursor.execute("SELECT logrole,logserver,logtype,loglevel,CAST(logdatetime AS CHAR),logdetail,logaction,logread FROM logapp_logtable where logrole='WEBSERVER' order by logdatetime desc limit 5")
	row = sqlcursor.fetchall()
	for data in row:
		strsplit = str(data).split("', '")
		pic = ""
		if (strsplit[3]=='Critical'):
			pic = "<img src='/static/images/critical.png' style='width:15px;height:15px;'>"
		elif(strsplit[3]=='Suspicious'):
			pic = "<img src='/static/images/warning.png' style='width:15px;height:15px;'>"
		else:
			pic = "<img src='/static/images/info.png' style='width:15px;height:15px;'>"
			
		all_result += "<tr onmouseover=\"this.style.backgroundColor='#ffff66';\" onmouseout=\"this.style.backgroundColor='#d4e3e5';\">"
		all_result += "<td>"+strsplit[1]+"</td><td>"+strsplit[4]+"</td><td>"+pic+" "+strsplit[5]+"</td><td>"+strsplit[6]+"</td>"
		all_result += "</tr>"
	conn.close()
	all_result += "</table>"
	return HttpResponse(all_result, content_type='text/html')

def fetch_web_item(request):
	all_result = ""
	conn = MySQLdb.connect(host= "mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
	sqlcursor = conn.cursor()
	sqlcursor.execute("SELECT CAST(id AS CHAR),CAST(logdatetime AS CHAR),logserver,logtype,loglevel,logdetail,logaction FROM logapp_logtable where logread='N' and logrole='WEBSERVER'")
	row = sqlcursor.fetchall()
	for data in row:
		strsplit = str(data).split("', '")
		temp = strsplit[1]+":"+strsplit[2]+":"+strsplit[3]+":"+strsplit[4]+":"+strsplit[5]+": action :"+strsplit[6]+"||"
		all_result += temp
		cmd = "update logapp_logtable set logread='Y' where id="+strsplit[0].replace("('","")
		sqlcursor.execute(cmd)
		conn.commit()
	conn.close()
	return HttpResponse(all_result, content_type='text/html')

def fetch_db(request):
	all_result ="<table class='hovertable'>"
	all_result += "<tr><th>Server Name </th><th>Log Time</th><th>Current Status</th><th>Action</th></tr>"
	conn = MySQLdb.connect(host= "mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
	sqlcursor = conn.cursor()
	sqlcursor.execute("SELECT logrole,logserver,logtype,loglevel,CAST(logdatetime AS CHAR),logdetail,logaction,logread FROM logapp_logtable where logrole='DBSERVER' order by logdatetime desc limit 5")
	row = sqlcursor.fetchall()
	for data in row:
		strsplit = str(data).split("', '")
		pic = ""
		if (strsplit[3]=='Critical'):
			pic = "<img src='/static/images/critical.png' style='width:15px;height:15px;'>"
		elif(strsplit[3]=='Suspicious'):
			pic = "<img src='/static/images/warning.png' style='width:15px;height:15px;'>"
		else:
			pic = "<img src='/static/images/info.png' style='width:15px;height:15px;'>"
			
		all_result += "<tr onmouseover=\"this.style.backgroundColor='#ffff66';\" onmouseout=\"this.style.backgroundColor='#d4e3e5';\">"
		all_result += "<td>"+strsplit[1]+"</td><td>"+strsplit[4]+"</td><td>"+pic+" "+strsplit[5]+"</td><td>"+strsplit[6]+"</td>"
		all_result += "</tr>"
	conn.close()
	all_result += "</table>"
	return HttpResponse(all_result, content_type='text/html')

def fetch_db_item(request):
	all_result = ""
	conn = MySQLdb.connect(host= "mysql-server",user="weblogadmin", passwd="admin123",db="weblog_db")
	sqlcursor = conn.cursor()
	sqlcursor.execute("SELECT CAST(id AS CHAR),CAST(logdatetime AS CHAR),logserver,logtype,loglevel,logdetail,logaction FROM logapp_logtable where logread='N' and logrole='DBSERVER'")
	row = sqlcursor.fetchall()
	for data in row:
		strsplit = str(data).split("', '")
		temp = strsplit[1]+":"+strsplit[2]+":"+strsplit[3]+":"+strsplit[4]+":"+strsplit[5]+": action :"+strsplit[6]+"||"
		all_result += temp
		cmd = "update logapp_logtable set logread='Y' where id="+strsplit[0].replace("('","")
		sqlcursor.execute(cmd)
		conn.commit()
	conn.close()
	return HttpResponse(all_result, content_type='text/html')
