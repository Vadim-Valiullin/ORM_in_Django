from django.core.management import BaseCommand
import json
from aaa.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:

            with open('aaa/csv_files/datasets/location.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    location_for_table = Location(
                        name=d['name'],
                        lat=d['lat'],
                        lng=d['lng'],
                    )
                    location_for_table.save()

            with open('aaa/csv_files/datasets/user.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    user_for_table = User(
                        first_name=d['first_name'],
                        last_name=d['last_name'],
                        username=d['username'],
                        password=d['password'],
                        role=d['role'],
                        age=d['age'],
                        # locations=Location.objects.get(d['location_id']),
                    )
                    user_for_table.save()

            with open('aaa/csv_files/datasets/categories.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    cat_for_table = Category(
                        name=d['name'],
                    )
                    cat_for_table.save()


            with open('aaa/csv_files/datasets/ads.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    ads_for_table = Ads(
                        name=d['name'],
                        author_id=d['author_id'],
                        price=d['price'],
                        description=d['description'],
                        is_published=d['is_published'].lower().title(),
                        image=d['image'],
                        category_id=d['category_id'],
                    )
                    ads_for_table.save()


            print('insert done')
        except:
            print('insert failed')

