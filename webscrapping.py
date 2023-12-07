import httpx
from bs4 import BeautifulSoup


response =httpx.get("https://www.fitnessblender.com/")
soup=BeautifulSoup(response.text,"html.parser")
# for i in soup.find_all("div","group responsive-media"):
#     print(i.find_all('img')['src'])

# print(str(soup.find("div","group responsive-media").find('img')['src']))

for i in (soup.find('section',"content-group -bg-02 -center -vs-large -hs-medium").find('div','group -full').find('div','vue cards').find_all('div','title-card-group')):
    print(i.find('div','card-content -with-extras'))