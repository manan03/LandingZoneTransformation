import json
from dictionary import dict1
from transform import transformit

# Read the JSON file
with open('temp1.json') as file:
    json_data2 = json.load(file)

# Convert JSON to string
json_string2 = json.dumps(json_data2)
 
if(json_string2.find('AutoScaling')!= -1):
    # Read the JSON file
    with open('AS.json') as file:
        json_data1 = json.load(file)

elif(json_string2.find('ElasticLoadBalancing')!= -1):
    # Read the JSON file
    with open('ELB.json') as file:
        json_data1 = json.load(file)
    
else:
    # Read the JSON file
    with open('EC2.json') as file:
        json_data1 = json.load(file)

 
version2 = json_data2["AWSTemplateFormatVersion"]
print(version2)
version1 = json_data1["AWSTemplateFormatVersion"]
print(version1)

if(version1 == version2):
    print("Up to date")
    transformit()
else:
    print("old")
    dict1[version1]=version2
    with open("find.py") as f:
        exec(f.read())
    transformit()


