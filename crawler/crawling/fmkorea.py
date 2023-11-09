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
            time = title.select_one('div > div:nth-child(4) > span.regdate')
            url = name.get('href')
            print(name.get_text().strip())
            print(shop.get_text().strip())
            print(price.get_text().strip())
            print(deliver.get_text().strip())
            print(time.get_text().strip())
            print(f"https://www.fmkorea.com/{url}")
            print('---------------------------')
fmkorea()

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
            url = name.get('href')
            result_dict = \
                {
                    'name': name.get_text().strip(),
                    'shop': shop.get_text().strip(),
                    'price': price.get_text().strip(),
                    'deliver': deliver.get_text().strip(),
                    'url': f"https://www.fmkorea.com/{url}"
                }
            result_list.append(result_dict)

        return result_list
