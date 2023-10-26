from bs4 import BeautifulSoup
import requests


def ruliweb():
    url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget > td > div > a.deco')
        for title in titles:
            print(title.text.strip())
            print('------------------------------')


def ruliweb_list():
    url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget > td > div > a.deco')
        result_list = []
        for title in titles:
            result_dict = \
                {
                    'name': title.text.strip()
                }
            result_list.append(result_dict)

        return result_list
