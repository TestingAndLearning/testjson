import urllib2, base64
import json
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

#This script gets all project IDs
#Put your API Key here
key = ""
#Put your url here minus the page number
purl = "https://a.teamwork.com/projects.json"

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
pname = {}

#Mapping Project ID to a company name. Also added project name.
for i in range (0, len(projnames['projects'])):
    d[projnames['projects'][i]['id']]= projnames['projects'][i]['company']['name']
    pname[projnames['projects'][i]['id']]= projnames['projects'][i]['name'] #Project name
    #print projnames['projects'][i]['name']

#Using these to store the project number and company name.
tempprojnumbers = ""
tempcompname = ""

#for i in range (0, len(projnames['projects'])):
#print projnames['projects'][i]['id']
#Converting the names to a string so that I can split them later and use for loop, since im not familiar with how python handles hashes/maps, lengths, loops and stuff. Remember to figure it out.
for pkey in d:
    tempprojnumbers = tempprojnumbers + pkey+","
    #Not sure if I even need this, since im using the hash anyway. Do I even need any of this???
    tempcompname = tempcompname + d[pkey]+","
    #print d[pkey]

print "Finished getting project numbers. "
#print tempprojnumbers

#This part saves the json data into the file.
#####

#Last one is an empty slot, remember to get rid of that or it might end in bad request error.
projnumbers = tempprojnumbers.split(",")
#tempcompname =

#Put your API Key here
#key = "aaa"
#Put your url here minus the page number
#print projnumbers

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

	#Checks if maximum page reached. Api gives that status below if there is no other page left.
        if data != "{\"activity\":[],\"STATUS\":\"OK\"}":
	    tempjson = tempjson + data
	    pagenumber += 1
	    print "Found Page " + str(pagenumber)
	else:
	    print "No pages left"
	    start = 0
	    #break
	time.sleep(1)

    pagenumber = 0
    start = 1
    progress = progress + 1
    #Find and replace Project ID part with both Project ID and Company Name in the tempjson string.
    tempjson = tempjson.replace("\"projectId\":\""+p+"\",","\"projectId\":\""+p+"\",\"company\":\""+d[p]+"\",\"projectName\":\""+pname[p]+"\",")
    print "Finished project " + p + " " + d[p] + " " + str(progress) + "/" + str(len(projnumbers))
    #Appends to the file, doesn't overwrite.
    f = open("outputrawdata.txt", "a")
    f.write(tempjson)
    f.close

    tempjson = ""

print "Task complete. "

#After this, run the bash script with sed to remove and replace unvalid json formatting that results from this whole process of appending different pages of json objects into a string format. Remember to learn more about json because I am pretty sure there is a better way on handling things here.
