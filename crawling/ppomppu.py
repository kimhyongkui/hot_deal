from bs4 import BeautifulSoup
import requests

def ppomppu():
    url = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')

        # # 필요한 부분을 가져온다
        # titles = soup.find_all('font', class_='list_title')
        # for title in titles:
        #     print(title.string)

        title = soup.select_one('#revolution_main_table > tbody > tr:nth-child(8)')
        print(title)

print(ppomppu())