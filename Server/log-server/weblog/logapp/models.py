from django.db import models
#from django.utils import timezone
import django
# Create your models here.
class logtable(models.Model):
	logserver = models.CharField(max_length=50)
	logdatetime = models.DateTimeField(default=django.utils.timezone.now)
	logtype = models.CharField(max_length=50)
	loglevel = models.CharField(max_length=50)
	logdetail = models.CharField(max_length=500)
	logread = models.CharField(max_length=1)
	logaction = models.CharField(max_length=100)
	logrole = models.CharField(max_length=50)
 
class listhostname(models.Model):
	listhost  = models.CharField(max_length=50)
	listip = models.CharField(max_length=50)
	listagent = models.CharField(max_length=20)
	liststatus = models.CharField(max_length=200)
	listaction = models.CharField(max_length=100)

class checktable(models.Model):
	serverrole = models.CharField(max_length=50)
	lastquery = models.DateTimeField(default=django.utils.timezone.now)
