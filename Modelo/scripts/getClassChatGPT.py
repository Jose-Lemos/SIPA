import requests
from bs4 import BeautifulSoup

url = "https://www.bas.ac.uk/"
response = requests.get(url)
content = response.content

print(response)
#print(content)

soup = BeautifulSoup(content, "html.parser")
tag = "article"
articles = soup.find_all(tag, class_="cust-col-4")

print(articles)

for article in articles:
    print(article.text.strip())