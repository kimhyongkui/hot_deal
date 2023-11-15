from bs4 import BeautifulSoup
import requests


def fmkorea():
    web_url = requests.get('https://www.fmkorea.com/hotdeal')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        for title in titles:
            name = title.select_one('div > h3 > a')
            shop = title.select_one('div > div > span:nth-child(1)')
            price = title.select_one('div > div > span:nth-child(2)')
            deliver = title.select_one('div > div > span:nth-child(3)')
            date = title.select_one('div > div > span.regdate')
            url = name.get('href')
            print(name.text.strip())
            print(shop.text.strip())
            print(price.text.strip())
            print(deliver.text.strip())
            print(date.text.strip())
            print(f"https://www.fmkorea.com/{url}")
            print('---------------------------')


def fmkorea_list():
    web_url = requests.get('https://www.fmkorea.com/hotdeal')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        result_list = []
        for title in titles:
            name = title.select_one('div > h3 > a')
            shop = title.select_one('div > div > span:nth-child(1)')
            price = title.select_one('div > div > span:nth-child(2)')
            deliver = title.select_one('div > div > span:nth-child(3)')
            date = title.select_one('div > div > span.regdate')
            url = name.get('href')
            result_dict = \
                {
                    'name': name.text.strip(),
                    'shop': shop.text.strip(),
                    'price': price.text.strip(),
                    'deliver': deliver.text.strip(),
                    'date': date.text.strip(),
                    'url': f"https://www.fmkorea.com/{url}"
                }
            result_list.append(result_dict)

        return result_list
