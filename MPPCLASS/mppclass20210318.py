import json
import os.path

#This code allow us get the current path where're this specific file
pwd = os.path.dirname(os.path.realpath(__file__))

#print(pwd)
def get_json_data():
    #o = open(f"{pwd}/data/data.json")
    json_file = open('data/data.json')

    data = json.load(json_file)
    data = data['data']
    #print(data[1])
    json_file.close()
    return data
    
#print(type(get_json_data()))

