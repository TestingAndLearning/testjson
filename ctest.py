import urllib2, base64
import json

#This script gets all project names

#Put your API Key here
key = "twp_jOjBYHjCGE0X99V9erF4NHtiaKmk"
#Put your url here minus the page number
url = "https://bsmall.teamwork.com/projects.json"

pagenumber = 0
tempjson = ""

#while start == 1
#pagenumber will increment at the end if a json result is found.
request = urllib2.Request(url.format())
request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

response = urllib2.urlopen(request)
data = response.read()

#Checks if maximum page reached.
projnames = json.loads(data)
#print projnames['projects'][0]['name']


for i in range (0, len(projnames['projects'])):
    print projnames['projects'][i]['name']

for i in range (0, len(projnames['projects'])):
    print projnames['projects'][i]['id']
