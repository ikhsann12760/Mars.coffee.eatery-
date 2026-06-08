from django.shortcuts import render
from .models import Menu, Category

def index(request):
    highlights = Menu.objects.filter(is_highlight=True)[:3]
    categories = Category.objects.all().prefetch_related('menus')
    
    context = {
        'highlights': highlights,
        'categories': categories,
    }
    return render(request, 'cafe/index.html', context)
