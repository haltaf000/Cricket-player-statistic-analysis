import requests
from bs4 import BeautifulSoup

url = "https://stats.espncricinfo.com/ci/engine/player/253802.html?class=1;template=results;type=batting;view=innings"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

article_tag = soup.getText()
print(article_tag)

    