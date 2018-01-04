import urllib2, base64
import json

#This script gets all project IDs
#Put your API Key here
key = "aaa"
#Put your url here minus the page number
purl = "https://asas.teamwork.com/projects.json"

ptempjson = ""

#while start == 1
#pagenumber will increment at the end if a json result is found.
prequest = urllib2.Request(purl.format())
prequest.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

presponse = urllib2.urlopen(prequest)
pdata = presponse.read()

#Checks if maximum page reached.
projnames = json.loads(pdata)
#print projnames['projects'][0]['name']

d = {}

for i in range (0, len(projnames['projects'])):
    d[projnames['projects'][i]['id']]= projnames['projects'][i]['name']
    #print projnames['projects'][i]['name']

tempprojnumbers = ""

#for i in range (0, len(projnames['projects'])):
    #print projnames['projects'][i]['id']
for pkey in d:
    tempprojnumbers = tempprojnumbers + pkey+",",


#This part saves the json data into the file. 
#####

projnumbers = "".split(",")

#Put your API Key here
#key = "aaa"
#Put your url here minus the page number
url1 = "https://asas.teamwork.com/projects/"
url2 = "/latestactivity.json?page="

pagenumber = 0
start = 1
tempjson = ""

for p in projnumbers:

	while start == 1:
	        #pagenumber will increment at the end if a json result is found.
	        request = urllib2.Request(url1+str(p)+url2+str(pagenumber).format())
	        request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

	        response = urllib2.urlopen(request)
	        data = response.read()

	        #Checks if maximum page reached.
	        if data != "{\"activity\":[],\"STATUS\":\"OK\"}":
	                tempjson = tempjson + data
	                pagenumber += 1
	                print "Found Page " + str(pagenumber)
	        else:
	                print "No page"
	                start = 0
	                #break
	print "Task completed"
	pagenumber = 0
	start = 1

	f = open("outputrawdata.txt", "a")
	f.write(tempjson)
	f.close

	tempjson = ""
