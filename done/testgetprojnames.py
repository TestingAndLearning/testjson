import urllib2, base64
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#This script gets all project IDs
#Put your API Key here
key = "jytyj"
#Put your url here minus the page number
purl = "https://fuyjfuyk.teamwork.com/projects.json"

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
    #Company names had a dash and activity after it, and some dont have space aftert he dash. Splitting to only get the Company Name.
    d[projnames['projects'][i]['id']]= projnames['projects'][i]['company']
    #print d[projnames['projects'][i]['id']]
    print projnames['projects'][i]['company']['name']
