from crawler.crawling.fmkorea import fmkorea_list
from crawler.crawling.ppomppu import ppomppu_list
from crawler.crawling.ruliweb import ruliweb_list
import schedule
import time


def update_data():
    schedule.every(6).hours.do(lambda: fmkorea_list())
    schedule.every(6).hours.do(lambda: ppomppu_list())
    schedule.every(6).hours.do(lambda: ruliweb_list())

    while True:
        schedule.run_pending()
        time.sleep(1)