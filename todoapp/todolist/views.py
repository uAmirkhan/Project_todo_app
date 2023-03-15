
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']  #
    todo = ToDo(title=title)
    todo.save()                    # сохранение бд
    return  redirect('index')      # возвращаемся на главную страницу

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)  #обращаемся к модели обьекта ищем по айди таску
    todo.is_complete = not todo.is_complete # поле "выполнено" в false
    todo.save()
    return redirect('index')

def delete(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete() # удаляем
    return redirect('index') # возвращаемся на главную