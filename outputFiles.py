import requests
from configparser import ConfigParser
from pprint import pprint
import datetime as dt
import json
import csv


exaatCredentials = r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\exxatCreds.txt'
runDateTime = dt.datetime.utcnow().strftime('%Y-%m-%d_T%H.%M.%S')

"""Set Up Output Files"""
siteTxtFile = r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\DataDumps\siteOutput_' + runDateTime + '.txt'
peopleTxtFile = r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\DataDumps\peopleOutput_' + runDateTime + '.txt'
studentTxtFile = r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\DataDumps\studentOutput_' + runDateTime + '.txt'

jsonOutputPath = r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\JSONFiles'

cfg = ConfigParser()
cfg.read(exaatCredentials)
apiKey = cfg.get('exxat', 'apiPrimaryKey')


"""Set up URLs"""
siteUrl = r'https://exxat-api-management.azure-api.net/Site'
studentUrl = r'https://exxat-api-management.azure-api.net/Student'
peopleUrl = r'https://exxat-api-management.azure-api.net/Person'




headers = {
    'Ocp-Apim-Subscription-Key' : apiKey
           }


def writeTxtFile(txtFile, header, url):
    print('Starting File Process ' + txtFile)
    r = requests.get(url, headers=header)
    print(r.status_code)
    print('Connected to ' + url + ' successfully.')
    data = r.json()
    writer = csv.writer(open(txtFile, 'a', encoding='utf8'), delimiter='|')

    siteHeader = []
    for item in data[0]:
        # print(item)
        siteHeader.append(item)
    writer.writerow(siteHeader)
    print('Header processing completed.')
    for row in data:
        block = []
        # print(row)
        for item in row:
            # print(row[item])
            value = row[item]
            value = str(value).replace("\r\n", " ")
            block.append(value)
        # print(block)
        writer.writerow(block)
    print('File has been written. ' + txtFile)
    print('***File Complete***')

#
# r = requests.get(siteUrl, headers=headers)
# # print(r.status_code)
# data = r.json()
# # print(data)
#
# with open(jsonOutputPath + '\siteOutput' + runDateTime + '.json', 'a') as siteOutput:
#     json.dump(data,siteOutput)




# with open(r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\JSONFiles\siteOutput2019-02-12_T16.11.00.json') as siteFile:
#     data = json.load(siteFile)
#
#
# writeTxtFile(siteTxtFile, data)


# r = requests.get(studentUrl, headers=headers)
# print(r.status_code)
# data = r.json()
# with open(jsonOutputPath + '\studentOutput' + runDateTime + '.json', 'a') as siteOutput:
#     json.dump(data,siteOutput)


#
# with open(r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\JSONFiles\studentOutput2019-02-12_T17.43.15.json') as siteFile:
#     data = json.load(siteFile)
#
#
# writeTxtFile(studentTxtFile, data)


# r = requests.get(peopleUrl, headers=headers)
# print(r.status_code)
# data = r.json()
# with open(jsonOutputPath + '\personOutput' + runDateTime + '.json', 'a') as siteOutput:
#     json.dump(data,siteOutput)



# with open(r'C:\Users\JefferyMcCain\Documents\PythonFiles\exxatAPI\OutputFiles\JSONFiles\personOutput2019-02-12_T18.24.46.json') as siteFile:
#     data = json.load(siteFile)


writeTxtFile(peopleTxtFile, headers, peopleUrl)

writeTxtFile(siteTxtFile, headers, siteUrl)

writeTxtFile(studentTxtFile, headers, studentUrl)
