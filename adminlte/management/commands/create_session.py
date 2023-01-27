import random

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from faker import Faker


from adminlte.models import Film, Hall, Session, Image, Gallery, SeoBlock

class Command(BaseCommand):
    help = 'Random session'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        film_id = Film.objects.all()
        hall_id = Hall.objects.all()
        for i in range(1, 50):
            Session.objects.create(id=i, day=fake.date_this_month(after_today=True),
                                   time_start=fake.time(pattern='%H:%M:%S'), film=random.choice(film_id),
                                   hall=random.choice(hall_id), type_2d=True, type_3d=False,
                                   type_imax=False)
        for i in range(50, 100):
            Session.objects.create(id=i, day=fake.date_this_month(after_today=True),
                                   time_start=fake.time(pattern='%H:%M:%S'), film=random.choice(film_id),
                                   hall=random.choice(hall_id), type_2d=False, type_3d=True,
                                   type_imax=False)
        for i in range(100, 150):
            Session.objects.create(id=i, day=fake.date_this_month(after_today=True),
                                   time_start=fake.time(pattern='%H:%M:%S'), film=random.choice(film_id),
                                   hall=random.choice(hall_id), type_2d=False, type_3d=False,
                                   type_imax=True)