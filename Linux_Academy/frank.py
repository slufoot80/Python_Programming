import urllib
import json

url = "https://labfiles.linuxacademy.com/python/ec2-response.json"
response = urllib.urlopen(url)
json_string = response.read()
print(json_string)

data = None
try:
    data = json.loads(str(json_string))
except:
    data = None

if ( data ):
    print("InstanceId %s is %s" (data['InstanceStatuses'][0]['InstanceId'], data['InstanceStatuses'][0]['InstanceState']['Name']))
