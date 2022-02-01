
import requests
import json
import datetime
import os

#카카오 토큰을 저장할 화일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"

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

def first_tokens():

    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : "8cc0852376ccb892823e5b1262d061ec",
        "redirect_uri" : "https://localhost.com",
        "code" : "lEu_63gQVHTcw2ThXA0WHhG2RMnMqNKcOHt3iIKBRKq2Zy3x_hmzv51zWkHg1aN_R3Ac4Qo9dBEAAAF-tfs6lA"
    }

    response = requests.post(url, data=data)

    # 요청에 실패했다면,
    if response.status_code != 200:
        print("error! because ", response.json())
        tokens = response.json()
    else: # 성공했다면,
        tokens = response.json()
        print(tokens)
    
    return tokens, response.status_code

# 새로운 토큰 호출
err_no = 0
tokens, err_no = first_tokens()
print("22 - error! because ", err_no)

if err_no != 200:
    # 토큰 업데이트 -> 토큰 저장 필수
    KAKAO_APP_KEY = "8cc0852376ccb892823e5b1262d061ec"
    tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
    # Refresh 토큰 저장
    save_tokens(KAKAO_TOKEN_FILENAME,tokens)
else:
    # first 토큰 저장
    save_tokens(KAKAO_TOKEN_FILENAME, tokens)


#저장된 토큰 정보를 읽어옴
tokens = load_tokens(KAKAO_TOKEN_FILENAME)

# 텍스트 메시지 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# requests parameter 설정
headers = {
    "Authorization": "Bearer " + tokens['access_token']
}

data = {
    "template_object" : json.dumps({ "object_type" : "text","text" : "Hello, world 2222!", "link" : {"web_url" : "www.naver.com"}})
}

# 나에게 카카오톡 메시지 보내기 요청(text)
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# 요청에 실패 했다면
if response.status_code != 200:
    print("error! because ", response.json)
else:
    print("message is sent succeessfully")
