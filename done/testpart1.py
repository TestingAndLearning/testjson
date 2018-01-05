import urllib2, base64
import json

#This script gets all project IDs
#Put your API Key here
key = "trshrt"
#Put your url here minus the page number
purl = "https://jdtyjydt.teamwork.com/projects.json"

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
    print projnames['projects'][i]['name'] + " " + projnames['projects'][i]['id']

tempprojnumbers = ""

#for i in range (0, len(projnames['projects'])):
    #print projnames['projects'][i]['id']

for pkey in d:
    tempprojnumbers = tempprojnumbers + pkey+","

print "Completed Task. "
