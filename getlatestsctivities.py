import urllib2, base64
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#This script gets all project IDs
#Put your API Key here
key = "bbb"
#Put your url here minus the page number
purl = "https://aaa.teamwork.com/projects.json"

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

#print projnames

print "Getting project numbers. "

d = {}

for i in range (0, len(projnames['projects'])):
    #Company names had a dash and activity after it, and some dont have space aftert he dash. Splitting to only get the Company Name.
    d[projnames['projects'][i]['id']]= projnames['projects'][i]['company']['name']
    #print projnames['projects'][i]['name']

tempprojnumbers = ""
tempcompname = ""

#for i in range (0, len(projnames['projects'])):
    #print projnames['projects'][i]['id']
for pkey in d:
    tempprojnumbers = tempprojnumbers + pkey+","
    tempcompname = tempcompname + d[pkey]+","
    print d[pkey]
    #Add temp name here

print "Finished getting project numbers. "
#print tempprojnumbers

#This part saves the json data into the file.
#####

projnumbers = tempprojnumbers.split(",")
#tempcompname =

#Put your API Key here
#key = "aaa"
#Put your url here minus the page number
url1 = "https://visiercorp.teamwork.com/projects/"
url2 = "/latestactivity.json?page="

pagenumber = 0
start = 1
tempjson = ""
progress = 0

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
	    print "No pages left"
	    start = 0
	    #break

    pagenumber = 0
    start = 1
    progress = progress + 1
    #Find and replace Project ID part with Project ID and Company Name in tempjson.
    tempjson = tempjson.replace("\"projectId\":\""+p+"\",","\"projectId\":\""+p+"\",\"company\":\""+d[p]+"\",")
    print "Finished project " + p + " " + d[p] + " " + str(progress) + "/" + str(len(projnumbers))
    f = open("outputrawdata.txt", "a")
    f.write(tempjson)
    f.close

    tempjson = ""

print "Task complete. "
