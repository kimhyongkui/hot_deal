from bs4 import BeautifulSoup
import requests


def ppomppu():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        for title in titles:
            name = title.select_one('a > font.list_title')
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            if name is not None:
                print(name.get_text().strip())
                if category is not None:
                    print(category.get_text().strip())
                else:
                    print("없음")
                print('------------------------------')
