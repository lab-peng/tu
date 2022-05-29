from django.core.management.base import BaseCommand
from django.utils import timezone


from app_c.models import Friend

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('I am here because you have typed "python manage.py exec" in command line interface')






