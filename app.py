import json

f = open('./provider.json')

# return json object as a dictionary
data = json.load(f)


# print entire json file
print(data)

# print data from the root element
for d in data['cloud_provider_details']:
        print(d)

# print the first element from each record
for d in data['cloud_provider_details']:
        print(d['cloud'])

# print the provider details if the cloud is GCP
for d in data['cloud_provider_details']:
        if d['cloud'] == "GCP":
                print(d['provider'])

f.close()