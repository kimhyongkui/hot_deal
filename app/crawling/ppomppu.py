from bs4 import BeautifulSoup
import requests
import schedule
import time


def ppomppu():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        for title in titles[3:42]:
            name = title.select_one('a > font.list_title')
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            if name is not None:
                print(name.get_text().strip())
                if category is not None:
                    print(category.get_text().strip())
                else:
                    print("없음")
                print('------------------------------')


def ppomppu_list():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        result_list = []
        for title in titles[3:42]:
            name = title.select_one('a > font.list_title')
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            if name is not None:
                if category is not None:
                    result_dict = \
                        {
                            'name': name.get_text().strip(),
                            'category': category.get_text().strip()
                        }
                else:
                    result_dict = \
                        {
                            'name': name.get_text().strip(),
                            'category': '없음'
                        }
                result_list.append(result_dict)

        return result_list


schedule.every(6).hours.do(lambda: ppomppu_list())

while True:
    schedule.run_pending()
    time.sleep(1)
