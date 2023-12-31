from bs4 import BeautifulSoup
import requests


def ppomppu():
    web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        dates = soup.select('td:nth-child(4) > nobr')
        numbers = soup.select('td.eng.list_vspace[colspan="2"]')
        for title, date, number in zip(titles[3:42:2], dates[1:22:1], numbers[6::4]):
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            name = title.select_one('a > font.list_title')
            date_text = date.text.strip()
            url = title.select_one('a').get('href')
            number_text = number.text.strip()
            if name is not None:
                print(category.text.strip())
                print(name.text.strip())
                print(date_text)
                print(f"https://www.ppomppu.co.kr/zboard/{url}")
                print(number_text)
                print('------------------------------')


def ppomppu_list():
    web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        dates = soup.select('td:nth-child(4) > nobr')
        numbers = soup.select('td.eng.list_vspace[colspan="2"]')
        result_list = []
        for title, date, number in zip(titles[3:42:2], dates[1:22:1], numbers[6::4]):
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            name = title.select_one('a > font.list_title')
            date_text = date.text.strip()
            url = title.select_one('a').get('href')
            number_text = number.text.strip()
            if name is not None:
                result_dict = \
                    {
                        'number': number_text,
                        'category': category.text.strip(),
                        'name': name.text.strip(),
                        'date': date_text,
                        'url': f"https://www.ppomppu.co.kr/zboard/{url}"
                    }
                result_list.append(result_dict)

        result_list = sorted(result_list, key=lambda x: x['number'])

        return result_list
