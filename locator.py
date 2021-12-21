import requests
import os
import sys
var1 = str(input('Please enter the ip: '))
response = requests.get("http://ip-api.com/json/"+var1+"").json()





print('Did it work? ' + response['status'])
print('What country? ' + response['country'])
print('What Province/State? ' + response['regionName'])
print('What city? '+response['city'])
print('Zip? '+response['zip'])
print('Timezone? '+response['timezone'])
print('Provider? '+response['as'])
print('Isp? '+response['isp'])
print(response['lat'])
print(response['lon'])
os.system('pause')
