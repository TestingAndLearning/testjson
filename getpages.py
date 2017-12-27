import urllib2, base64
import json

#Put your API Key here
key = "twp_jOjBYHjCGE0X99V9erF4NHtiaKmk"
#Put your url here minus the page number
url = "https://bsmall.teamwork.com/projects/268622/tasks.json"

pagenumber = 0
start = 1
tempjson = ""

while start == 1
	#pagenumber will increment at the end if a json result is found.
	request = urllib2.Request(url+str(pagenumber).format())
	request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

	response = urllib2.urlopen(request)
	data = response.read()

	#Checks if maximum page reached.
	if data != "200 ok":
		tempjson = tempjson + data
		pagenumber += 1
	else:
		start = 0
		pagenumber = 0
		break
		
pagenumber = 0
print "Task completed"

#write to the file.
f = open("testfile.txt", "w")
f.write(tempjson)
f.close
