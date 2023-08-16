from bs4 import BeautifulSoup
import requests


def ruliweb():
    url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        board = soup.select('tbody > tr.table_body.blocktarget > td > div > a.deco')
        for title in board:
            print(title.text.strip())
            print('------------------------------')
