import os
import sys


# def main():
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hot_deal.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
#
# if __name__ == '__main__':
#     main()

if __name__ == '__main__':
    # 개발 환경일 때
    if 'development' in sys.argv:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hot_deal.settings.development')
    # 프로덕션 환경일 때
    elif 'production' in sys.argv:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hot_deal.settings.production')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)