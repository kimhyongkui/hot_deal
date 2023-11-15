from bs4 import BeautifulSoup
import requests


def ruliweb():
    web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget')
        for title in titles[4:32]:
            category = title.select_one('td.divsn.text_over > a[tabindex="-1"]')
            name = title.select_one('td.subject > div > a.deco')
            date = title.select_one('td.time')
            url = title.select_one('td.subject > div > a.deco').get('href')
            print(category.text.strip())
            print(name.text.strip())
            print(date.text.strip())
            print(url)
            print('------------------------------')


def ruliweb_list():
    web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget')
        result_list = []
        for title in titles[4:32]:
            category = title.select_one('td.divsn.text_over > a[tabindex="-1"]')
            name = title.select_one('td.subject > div > a.deco')
            date = title.select_one('td.time')
            url = title.select_one('td.subject > div > a.deco').get('href')
            result_dict = \
                {
                    'category': category.text.strip(),
                    'name': name.text.strip(),
                    'date': date.text.strip(),
                    'url': url
                }
            result_list.append(result_dict)

        return result_list
