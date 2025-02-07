import requests
from bs4 import BeautifulSoup
url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

print(soup.prettify())

# парсинг с помощьюю html.parser
url = "https://matplotlib.org/stable/gallery/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify()) # распечатка переменной в красивом виде

lst = soup.find_all('h2')

# функция выделения заголовков из текста
def clean_item(my_item):
    position = my_item.find('<a')
    return my_item[4:position]
#проверка функции выделения заголовков из текста
print(clean_item('<h2>Images, contours and fields<a class'))

#пройдемся по списку lst используя функцию  в цикле для получения заголовков
for item in lst:
    print(clean_item(str(item)))
    
# парсинг раздела примеров Seaborn
url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

lst2 = soup.find_all("p")

def clean_item2(my_item2):
    position2 = my_item2.find('</p')
    return my_item2[3:position2]

# получаем список , используя цикл
for item2 in lst2:
    print(clean_item2(str(item2)))
