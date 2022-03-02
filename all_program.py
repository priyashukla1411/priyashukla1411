import requests
import json
url = "https://www.fast2sms.com/dev/bulk"
my_data = {

	'sender_id': 'FSTSMS',
	

	'message': 'hello ',
	
	'language': 'english',
	'route': 'p',

	'numbers': '9988154389'	}
headers = {
	'authorization': 'moYvjT7tBylP5iWJkS8ecGs6LIN4hMb3wVCpnurqE2xADFUdX9uL4HzSshPCMoANlrf96R8YOFcjVnQe',

}
response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)

returned_msg = json.loads(response.text)
#tdfgfhg
  

print(returned_msg['hello'])
