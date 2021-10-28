import requests;
from bs4 import BeautifulSoup;

resp = requests.get("https://search.naver.com/search.naver?query=강남구+날씨")
if resp.status_code == 200:
   	html = resp.text


#HTML안에 위 내용이 들어가 있다고 가정.
soup = BeautifulSoup(html,"html.parser")

box = soup.find("div",{"class":"temperature_text"}).text


print(box)
