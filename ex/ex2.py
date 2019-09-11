from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.daum.net/").read()
soup = BeautifulSoup(html, "html.parser")
myUrls = soup.select('span.txt_issue')
cnt = 0
for j in myUrls:
    cnt +=1
    print(str(cnt)+". "+j.text)
    if cnt==20:
        break