import requests 
import os,sys
import datetime

object_name = sys.argv[1]

url_file= open(object_name, 'r')
image_dir = "imagenet/"+object_name+"/"

if not os.path.exists(image_dir):
	os.mkdir(image_dir)

for line in url_file.read().split('\n'):
	if line != "" and "static.flickr.com" not in line:
		url = line
		#print url
		try:
			r = requests.get(url) 
			if "Not Found" in r.content:
				print "[%s][Not Found]: %s" %(datetime.datetime.now(), url)
			else:
				with open(image_dir+url.split("/")[-1], "wb") as code:
					code.write(r.content)
				print "[%s][Downloaded]: %s" %(datetime.datetime.now(), url)
		except Exception as e:
			print "[%s][Time Out]: %s" %(datetime.datetime.now(), url)

