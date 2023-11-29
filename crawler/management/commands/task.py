from django.core.management.base import BaseCommand
from crawler.db.post.crawling_data import save_data_fmkorea, save_data_ppomppu, save_data_ruliweb
import schedule
import time


class Command(BaseCommand):
    help = 'Update data'

    def handle(self, *args, **options):
        schedule.every(1).minute.do(lambda: save_data_fmkorea())
        schedule.every(1).minute.do(lambda: save_data_ppomppu())
        schedule.every(1).minute.do(lambda: save_data_ruliweb())

        while True:
            schedule.run_pending()
            time.sleep(1)
