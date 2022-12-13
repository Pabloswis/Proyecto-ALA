from django.shortcuts import render
from apps.noticia.models import Noticia
from django.views.generic import ListView
# def principal(request):
#     return render(request, 'index.html')

# def nosotros(request):
#     return render(request, 'nosotros.html')

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'Index.html'