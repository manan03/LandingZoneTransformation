import json
import re
from dictionary import dict1

def UncommonWords(A, B):
    count = {}
    for word in A.split():
        count[word] = count.get(word, 0) + 1
    for word in B.split():
        count[word] = count.get(word, 0) + 1
    return [re.findall(r'"([^"]*)"', word)[0] for word in count if count[word] == 1]


# Read the JSON data from temp2.json
with open('temp1.json') as file:
    json_data2 = json.load(file)

# Convert JSON data to a string
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

# Convert JSON data to a string
json_string1 = json.dumps(json_data1)


# Pass the JSON strings to the UncommonWords function and print the result
result = UncommonWords(json_string1, json_string2)
# print("Uncommon Words:", result)

version = json_data1["AWSTemplateFormatVersion"]
 
version1 =  json_data2["AWSTemplateFormatVersion"]
for i in range(len(result)//2):
    if(result[i + len(result)//2]==  version1):
        continue
    dict1[result[i + len(result)//2]] = dict1[result[i]]

with open('dictionary.py', 'w') as file:
    file.write("dict1 = " + json.dumps(dict1, indent=4))

# print(dict1)