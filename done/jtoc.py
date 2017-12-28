import json

import csv

with open('testfile.json', 'r') as myfile:
    jsontext=myfile.read().replace('\n', '')

project_parsed = json.loads(jsontext)
p_data = project_parsed['todo-items']
# open a file for writing
proj_data = open('ProjData.csv', 'w')
# create the csv writer object
csvwriter = csv.writer(proj_data)

count = 0

for p in p_data:

      if count == 0:

             header = p.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(p.values())

proj_data.close()
