import requests
import json

def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    # request succeed
    if img_response.status_code == 200:
        # Save file
        with open(file_name,'wb') as fp:
            fp.write(img_response.content)



# 이미지 검색 
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization": "KakaoAK 8cc0852376ccb892823e5b1262d061ec"
}
data = {
    "query" : "키이라 나이틀리" , 
    "sort"  : "accuracy",
    "page"  : "1" ,
    "size"  : "10"
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ",  response.json())
else: # 성공했다면,
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        # 저장될 이미지 파일명 설정
        count = count + 1

        file_name = "test_%d.jpg" %(count)
        # call save image fnc
        save_image(image_info['image_url'], file_name)
