from django.core.management.base import BaseCommand
from crawler.crawling.count_and_notify import count_list
import schedule
import time


class Command(BaseCommand):
    help = 'Update data'

    def handle(self, *args, **options):
        schedule.every(1).minute.do(lambda: count_list("fmkorea"))
        schedule.every(1).minute.do(lambda: count_list("ppomppu"))
        schedule.every(1).minute.do(lambda: count_list("ruliweb"))

        while True:
            schedule.run_pending()
            time.sleep(1)
