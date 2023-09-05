from bs4 import BeautifulSoup
import requests
import schedule
import time


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


def fmkorea_list():
    url = requests.get('https://www.fmkorea.com/hotdeal')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        result_list = []
        for title in titles:
            result_dict = \
                {
                    'name': title.select_one('div > h3 > a').get_text().strip(),
                    'shop': title.select_one('div > div > span:nth-child(1)').get_text().strip(),
                    'price': title.select_one('div > div > span:nth-child(2)').get_text().strip(),
                    'deliver': title.select_one('div > div > span:nth-child(3)').get_text().strip()
                }
            result_list.append(result_dict)

        return result_list



schedule.every(1).hourss.do(fmkorea_list)

while True:
    schedule.run_pending()
    time.sleep(1)