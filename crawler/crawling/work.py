from crawler.db.post.crawling_data import save_data_fmkorea, save_data_ppomppu, save_data_ruliweb
import schedule
import time


def update_data():
    schedule.every(6).hours.do(lambda: save_data_fmkorea())
    schedule.every(6).hours.do(lambda: save_data_ppomppu())
    schedule.every(6).hours.do(lambda: save_data_ruliweb())

    while True:
        schedule.run_pending()
        time.sleep(1)
