"""
 NX-API-BOT 
"""
import requests
import json

"""
Modify these please
"""
url='http://10.255.0.94/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show vlan",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# parse through relevant JSON output to get currently used
#   vlan numbers.  Print out the highest + 1 as the next
#   available vlan number to use.

vlans = []
for item in response['result']['body']['TABLE_mtuinfo']['ROW_mtuinfo']:
    vlans.append(item['vlanshowinfo-vlanid'])

print(vlans[-1] + 1)
