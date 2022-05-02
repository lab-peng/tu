from django.core.management.base import BaseCommand
from django.utils import timezone


from app_c.models import Friend

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        friends = Friend.objects.all()
        count = Friend.objects.count()
        for f in friends:
            f.lives_in = 'New York'
            f.save()
            print(f.__dict__)






