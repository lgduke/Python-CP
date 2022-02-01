import requests

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