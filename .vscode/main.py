import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8&vjk=aac8e9355cb855ac")

indeed_soup = BeautifulSoup(indeed_result.text,'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})
print(pagination)

pages = pagination.find_all('a')

for page in pages:
  print(page.find("span"))