import json
import yaml

with open('myfile_12214756.json','r') as json_file:
 ourjson = json.load(json_file)

print(ourjson)

print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))
print("The refresh token is: {}".format(ourjson['refresh_token']))
print("The refresh token expires in {} seconds.".format(ourjson['refreshtokenexpires_in']))