import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvreader = csv.DictReader(csvf, delimiter=',')

        # convert each csv row into python dict
        for row in csvreader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = '/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.csv'
jsonFilePath = '/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.json'
csv_to_json(csvFilePath, jsonFilePath)

