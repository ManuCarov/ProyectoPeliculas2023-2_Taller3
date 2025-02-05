from django.core.management.base import BaseCommand
from recomendaciones.models import Recomendaciones
import json

class Command(BaseCommand):
    help = 'Modify path of images'

    def handle(self, *args, **kwargs):
        items = Recomendaciones.objects.all()
        for item in items:
            item.image.name = f"{item.image.name[0:13]}{item.title}.jpg" 
            item.save()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated with the illustrations of the movies'))
        