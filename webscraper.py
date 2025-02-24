import requests
from bs4 import BeautifulSoup

response=requests.get('https://www.bbc.com/news')

soup=BeautifulSoup(response.content,'html.parser')

headlines=soup.find_all('h2')

for headline in headlines:
    print(headline.text,"\n")
