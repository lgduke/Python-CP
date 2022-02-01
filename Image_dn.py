import requests

# image가 있는 URL 주소

url = "https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/news/7548a600017e00001.JPG"

# 해당 URL을 서버에게 요청
img_response = requests.get(url)

# 요청에 성공했다면
if img_response.status_code == 200:
#    print(img_response.content)

    print("Save Image")
    with open("test1.jpg","wb") as fp:
        fp.write(img_response.content)