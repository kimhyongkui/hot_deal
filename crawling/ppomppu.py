from bs4 import BeautifulSoup
import requests


def ppomppu():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('font', class_='list_title')
        for title in titles[1:]:
            print(title.text.strip())
