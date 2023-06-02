import json
from dictionary import dict1

def transformit():
    # Read the JSON file
    with open('temp1.json') as file:
        json_data = json.load(file)

    # Convert JSON to string
    json_string = json.dumps(json_data)


    for key, value in dict1.items():
        json_string = json_string.replace('"'+key+'"', '"'+value+'"')

    # print(json_string)

    def string_to_json_file(json_string, file_path):
        # Convert the JSON string back to a Python object
        json_data = json.loads(json_string)

        # Write the JSON data to a file
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)

        return file_path

    output_file = 'temp2.json'
    json_file_path = string_to_json_file(json_string, output_file)
    print("JSON file created")

    return
