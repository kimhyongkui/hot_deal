from bs4 import BeautifulSoup
import requests



def fmkorea():
    url = requests.get('https://www.fmkorea.com/hotdeal')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        for title in titles:
            name = title.select_one('div > h3 > a').get_text().strip()
            shop = title.select_one('div > div > span:nth-child(1)').get_text().strip()
            price = title.select_one('div > div > span:nth-child(2)').get_text().strip()
            deliver = title.select_one('div > div > span:nth-child(3)').get_text().strip()
            print(name)
            print(shop)
            print(price)
            print(deliver)
            print('---------------------------')