from bs4 import BeautifulSoup
import requests
import lxml

word = input()
url = ('http://alldic.daum.net/search.do?q={}'.format(word))
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
means = soup.select('.cleanword_type.kuek_type .list_search')

for i in means:
    print(i.text)

    with open('dictionary', 'w') as f:
        f.write(word)
        f.write(str(i.text))

