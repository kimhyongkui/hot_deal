# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")
#
# import django
#
# django.setup()
#
# from crawler.notification.discord_noti import send_discord_notification
# from crawler.crawling.ruliweb import ruliweb_list, save_ruliweb_list
#
# def count_and_notify(site_name, new_post_count, message_list):
#     if new_post_count >= 0:
#         message_list.append(f"{site_name} : {new_post_count}개 업데이트")
#         send_discord_notification(message_list)
#
#
# def count_result_list():
#     data_list = ruliweb_list()
#     new_post_count = 0
#     message_list = []
#     site_name = 'ruliweb'
#     for data in data_list:
#         save_ruliweb_list(data)
#         message_list.append(f"{data['name']}")
#         new_post_count += 1
#
#     count_and_notify(site_name, new_post_count, message_list)
#
# count_result_list()