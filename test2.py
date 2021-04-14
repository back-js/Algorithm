import requests

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

payload="<speak> 그는 그렇게 말했습니다. </speak>"
headers = {
  'Content-Type': 'application/xml',
  'Authorization': 'KakaoAK 264fb41b81e56fae1b785fafb9111a9b'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)