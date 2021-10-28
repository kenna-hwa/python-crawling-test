import requests;
from bs4 import BeautifulSoup;

resp = requests.get("https://bvoat.com/myshop/buy_records/list_all.html")
if resp.status_code == 200:
   	html = resp.text

print(resp.status_code)

#HTML안에 위 내용이 들어가 있다고 가정.
#soup = BeautifulSoup(html,"html.parser")

#box = soup.find("div",{"class":"cont_content"}).text



