from django.core.management.base import BaseCommand
from crawler.crawling.fmkorea import count_fmkorea_list
from crawler.crawling.ppomppu import count_ppomppu_list
from crawler.crawling.ruliweb import count_ruliweb_list
import schedule
import time


class Command(BaseCommand):
    help = 'Update data'

    def handle(self, *args, **options):
        schedule.every(1).minute.do(lambda: count_fmkorea_list())
        schedule.every(1).minute.do(lambda: count_ppomppu_list())
        schedule.every(10).seconds.do(lambda: count_ruliweb_list())

        while True:
            schedule.run_pending()
            time.sleep(1)
