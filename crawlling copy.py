import requests;


resp = requests.get("https://search.naver.com/search.naver?query=강남구+날씨")
if resp.status_code == 200:
   	html = resp.text

print(html)