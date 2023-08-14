from bs4 import BeautifulSoup
import requests


def fmkorea():
    url = requests.get('https://www.fmkorea.com/hotdeal')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        for title in titles:
            name = title.select_one('div > h3 > a')
            shop = title.select_one('div > div > span:nth-child(1)')
            price = title.select_one('div > div > span:nth-child(2)')
            deliver = title.select_one('div > div > span:nth-child(3)')
            print(name.get_text().strip())
            print(shop.get_text().strip())
            print(price.get_text().strip())
            print(deliver.get_text().strip())
            print('---------------------------')
