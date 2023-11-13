from bs4 import BeautifulSoup
import requests


# def ppomppu():
#     web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
#     if web_url.status_code == 200:
#         html = web_url.text
#         soup = BeautifulSoup(html, 'html.parser')
#         titles = soup.select('tr td:nth-child(2) > div')
#         dates = soup.select('td:nth-child(4) > nobr')
#         for title in titles[3:42]:
#             name = title.select_one('a > font.list_title')
#             category = title.select_one('span[style="color:#999;font-size:11px;"]')
#             url = title.select_one('a').get('href')
#             if name is not None:
#                 print(dates)
#                 print(name.get_text().strip())
#                 print(f"https://www.ppomppu.co.kr/zboard/{url}")
#                 print(category.get_text().strip())
#                 print('------------------------------')
def ppomppu():
    web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        dates = soup.select('td:nth-child(4) > nobr')
        for i, (title, date) in enumerate(zip(titles[3:42], dates[1:35])):
            name = title.select_one('a > font.list_title')
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            url = title.select_one('a').get('href')
            date_text = date.get_text().strip()
            if name is not None:
                print(date_text)
                print(name.get_text().strip())
                print(f"https://www.ppomppu.co.kr/zboard/{url}")
                print(category.get_text().strip())
                print('------------------------------')

ppomppu()
#revolution_main_table > tbody > tr:nth-child(9) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
#revolution_main_table > tbody > tr:nth-child(9) > td:nth-child(4) > nobr
#revolution_main_table > tbody > tr:nth-child(11) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
#revolution_main_table > tbody > tr:nth-child(11) > td:nth-child(4) > nobr
#revolution_main_table > tbody > tr:nth-child(13) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
#revolution_main_table > tbody > tr:nth-child(13) > td:nth-child(4) > nobr


def ppomppu_list():
    web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        result_list = []
        for title in titles[3:42]:
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            name = title.select_one('a > font.list_title')
            url = title.select_one('a').get('href')
            if name is not None:
                result_dict = \
                    {
                        'category': category.get_text().strip(),
                        'name': name.get_text().strip(),
                        'url': url
                    }
                result_list.append(result_dict)

        return result_list
