'''
Converts sample csv data to JSON array
:param Input .csv filepath, output .json filepath
:returns JSON Object array
'''
import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    jsonStringArray = []
    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvreader = csv.DictReader(csvf, delimiter=',', quoting=csv.QUOTE_ALL)

        # convert each csv row into python dict
        for row in csvreader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=0)
        jsonf.write(jsonString)
        jsonStringArray.append(jsonString)
    arr = json.loads(jsonStringArray[0])

    return arr


#csvFilePath = '/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.csv'
#jsonFilePath = '/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.json'
#csv_to_json(csvFilePath, jsonFilePath)

