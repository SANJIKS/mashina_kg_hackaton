import csv

from bs4 import BeautifulSoup
import requests

URL = 'https://www.mashina.kg/search/all/'

response = requests.get(URL)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_="list-item list-label")

result = []
for tag in cards:
    title = tag.find('div', class_='block title').text
    price = tag.find('div', class_='block price').text
    img = tag.find('div', class_='image-wrap')
    desc = tag.find('div', class_="block info-wrapper item-info-wrapper").text

    obj = {
        'title': title.strip(),
        'price': price.strip(),
        'discription': desc.strip().split('\n'),
        'image link': img,

    }
    result.append(obj)


with open('cars.csv', 'w+') as file:
    names = ['title', 'price', 'discription', 'image link']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for car in result: 
        writer.writerow(car)