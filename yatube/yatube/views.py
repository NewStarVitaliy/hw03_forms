from django.http import HttpResponse
from django.shortcuts import render
 

# Главная страница


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Словарь с данными принято называть context
    context = {
        'title': "Это главная страница проекта Yatube"
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        'title': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()


def icecream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
# Create your views here.
