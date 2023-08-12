from bs4 import BeautifulSoup
import requests


def fmkorea():
    url = requests.get('https://www.fmkorea.com/hotdeal')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li')
        for title in titles:
            name = title.select('div > h3 > a')
            shop = title.select('div > div > span')[0:1]
            price = title.select('div > div > span')[1:2]
            deliver = title.select('div > div > span')[2:3]
            print(name)
            print(shop)
            print(price)
            print(deliver)
            print("-----------------------------------------")

def fmkorea2():
    url = requests.get('https://www.fmkorea.com/hotdeal')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('li', class_='li li_best2_pop0 li_best2_hotdeal0')
        # titles = soup.find_all('li', class_="li  li_best2_pop0 li_best2_hotdeal0")
        # print(titles)
        for title in titles:
            title = title.find('h3', class_='title')
            shop = title.find('a')
            # price = title.find('div', class_='hotdeal_info')
            price = title.find(css='div > div.hotdeal_info > span:first-child > a')
            deliver = title.find('div', class_='hotdeal_info')
            print(price)
            # print(title.text.strip())
            # print(shop.text.strip())
            # print(price.text.strip())
            # print(deliver.text.strip())
            print("-----------------------------------------")

fmkorea2()


#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li:nth-child(1) > div > div.hotdeal_info > span:nth-child(1) > a