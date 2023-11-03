from django.shortcuts import render
from .models import recomendaciones

def recomendaciones(request):
    recomendacion = Recomendaciones.objects.all().order_by('-date')
    return render(request, 'recomendaciones.html', {'recomendacion':recomendacion})

