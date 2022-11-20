import csv
import json

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('app/csv_files/datasets/ads.csv', encoding='utf-8') as csv_ads:
            with open('app/csv_files/datasets/ads.json', 'w', encoding='utf-8') as js_ads:
                json.dump(list(csv.DictReader(csv_ads)), js_ads, ensure_ascii=False)

        with open('app/csv_files/datasets/categories.csv', encoding='utf-8') as csv_cat:
            with open('app/csv_files/datasets/categories.json', 'w', encoding='utf-8') as js_cat:
                json.dump(list(csv.DictReader(csv_cat)), js_cat, ensure_ascii=False)

        with open('app/csv_files/datasets/location.csv', encoding='utf-8') as csv_location:
            with open('app/csv_files/datasets/location.json', 'w', encoding='utf-8') as js_location:
                json.dump(list(csv.DictReader(csv_location)), js_location, ensure_ascii=False)

        with open('app/csv_files/datasets/user.csv', encoding='utf-8') as csv_user:
            with open('app/csv_files/datasets/user.json', 'w', encoding='utf-8') as js_user:
                json.dump(list(csv.DictReader(csv_user)), js_user, ensure_ascii=False)



