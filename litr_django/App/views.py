from django.shortcuts import render

def index(request):
    '''то, что мы возвращаем на фронт на глувную страницу,
        тут это название страницы и заголовок,
        но это можно поменять'''
    context = {
        'pagename': 'Lorem ipsum dolor sit amet'
    }
    return render(request, 'index.html', context) #отправка данных на фронт
