from django.core.management.base import BaseCommand
from recomendaciones.models import Recomendaciones
import json
import os
import numpy as np

class Command(BaseCommand):
    help = 'Modify path of images'

    def handle(self, *args, **kwargs):
  
        items = Recomendaciones.objects.all()
        item = items[10]
        print(item.emb)
        
        