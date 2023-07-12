from django.shortcuts import render
from .models import LinkModel

def index(request):
    links = LinkModel.objects.all()
    return render(request, 'SiteApp/index.html', context={'links': links})
