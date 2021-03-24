import requests
import json

kakao_tts_url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
rest_api_key = 'KakaoAK 264fb41b81e56fae1b785fafb9111a9b'

headers = {
'Content-Type': 'application/xml',
'Authorization': rest_api_key,
}

data = {
"<speak> <voice name='MAN_DIALOG_BRIGHT'>잘 지냈어? 나도 잘 지냈어.</voice>  </speak>"
}

response = requests.post(kakao_tts_url, headers=headers, data=data)
rescode = response.status_code

if(rescode==200):
    print('TTS mp3 저장')
    response_body = response.read()
    with open('result.mp3', 'wb') as f:
        f.write(response_body)
else:
    print('Error Code:'+str(rescode))

print(response.content)