from bs4 import BeautifulSoup
import requests


def ppomppu1():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find('table', id='revolution_main_table')
        for title in titles.select('tr:not(#page_show_noti_1)'):
            efg = title.find('font', class_='list_title')

            if efg:
                print(efg.text.strip())


def ppomppu2():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find('table', id='revolution_main_table')
        font_elements = titles.find_all('font', class_='list_title')
        for efg in font_elements[1:]:
            print(efg.text.strip())


def ppomppu3():
    url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', id='revolution_main_table')
        for row in table.find_all('tr'):
            data = row.select('#page_show_noti_1 > td:nth-child(3) > a > font')
            if not data:
                target_td = row.find('font', class_='list_title')
                if target_td:
                    print(target_td.text.strip())


def ppomppu4():
    url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=4')
    if url.status_code == 200:
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('font', class_='list_title')
        for title in titles:
            print(title.text.strip())
