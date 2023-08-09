from bs4 import BeautifulSoup
import requests


def ruliweb():
    url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        board = soup.find_all('a', class_='deco')
        for title in board[8:36]:
            result = title
            print(result.text.strip())
