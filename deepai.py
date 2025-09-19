import requests

url = "https://api.deepai.org/api/text2img"
api_key = "81b9db52-fcc4-4a61-a56c-0ab92d724b28"
data = { 'text': 'Een fotorealistisch portret van een lachende persoon in natuurlijk licht.' }

response = requests.post(url, data=data, headers={'api-key': api_key})
print("Code", response.status_code)
print("Response", response)

print(response.json())


#niet gratis!!