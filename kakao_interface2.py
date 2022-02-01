import json
from urllib import response
import requests
import datetime
import os


# 저장하는 함수
def save_tokens(filename, tokens):
    with open(filename,"w") as fp:
        json.dump(tokens, fp)

# 읽어오는 함수
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens

# refresh token으로 access token 갱신하는 함수
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"

    data = {
    "grant_type" : "refresh_token",
    "client_id" : app_key,
    "refresh_token" : tokens['refresh_token']
    }

    response = requests.post(url, data=data)

    # 요청에 실패했다면
    if response.status_code != 200:
        print("error! because ", response.json())
        tokens = None
    else: # 성공했다면
        print(response.json())
        # 기존 화일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename+"."+ now
        os.rename(filename, backup_filename)

        #갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
    
    return tokens

#카카오 토큰을 저장할 화일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "8cc0852376ccb892823e5b1262d061ec",
    "redirect_uri" : "https://localhost.com",
    "code" : "3-4yylADFKjDX3UU3J8lA6_TZrofmrRtvzvPv3T31Eav8-HZjmFxwRYiz4SzZXDDIBDzogo9dZsAAAF-pgu6xA"
}

response = requests.post(url, data=data)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else: # 성공했다면,
    tokens = response.json()
    print(tokens)

# 토큰 저장
save_tokens(KAKAO_TOKEN_FILENAME, tokens)

# 토큰 업데이트 -> 토큰 저장 필수
#KAKAO_APP_KEY = "8cc0852376ccb892823e5b1262d061ec"
#tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
#save_tokens(KAKAO_TOKEN_FILENAME,tokens)


