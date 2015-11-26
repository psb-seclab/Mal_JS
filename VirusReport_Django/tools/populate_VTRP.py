import simplejson
import urllib
import urllib2
import json
import time


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','VirusReport_Django')

import django
django.setup()

from virusList.models import Virus


def populate():
	#from datetime import datetime
	#generate file path day be day
	'''
	now=datetime.now();
	day=str(now.day-1);
	if (len(day)==1):
		day='0'+day;
	mon=str(now.month);
	if (len(mon)==1):
		mon='0'+mon;
	dirName=str(now.year)+"-"+mon+"-"+day
	'''
	MAL_DIR = '/root/JS_repository/2015-11-14'
	print MAL_DIR
	dirs=os.listdir(MAL_DIR)
	#send malicious html found by MALTRIEVE to VIRUSTOTAL to scan
	for f in dirs:
		time.sleep(15)
		path=MAL_DIR
		md5=f
		#print f
		rp=get_report_dict(md5)

		#detection
		detection=rp["scans"]
		holder=""
		for i in detection:
			if detection[i]['detected']==True:
				holder=holder+i+": "+str(detection[i]['result']+"<br />")
				
		add_virus(
			md5=md5,
			size=sizeOf(path),
			url=rp["permalink"],
			detection=holder
			)
		print holder
		
		

#===================================================================
def add_virus(md5,size,url,detection):
	v=Virus.objects.get_or_create(MD5=md5,size_KB=size)[0]
	v.VirusTotal_link=url
	v.Detection=detection
	v.save()
	return v;


#===================================================================
# Get size of the file named by MD5
def sizeOf(PATH):
	return (os.path.getsize(PATH)/1024.0)



#===================================================================
#Download report from virusTotal 
def get_report_dict(resource):

    result_dict = {}
    APIKEY="659fd24c11e839f866f32b0dfa37887e91d6713439505e717541595252d3c47f"
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": resource,
                   "apikey": APIKEY}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()

    #print json
    response_dict = simplejson.loads(json,"utf-8")
    
    return response_dict;


if __name__ == '__main__':
	print "Starting VirusList population script..."
	populate()