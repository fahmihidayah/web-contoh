from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

from .forms import TodoForm, TodoModelForm
from .models import Todo

# Create your views here.


class IndexCoba(TemplateView):
    template_name = "todos/index_todo.html"

    def get(self, request, *args, **kwargs):
        print('get request method called ')
        return HttpResponse('hallo abc')



def index(request):
    return HttpResponse('hallo fahmi')


def penjumlahan(request, angka1, angka2):
    if request.method == 'GET':
        print('get method called')

    total = angka1 + angka2
    return HttpResponse('Hasil adalah ' + str(total))


def contoh_html(req):
    contoh(nama='fahmi')
    return render(request=req, template_name='hello.html')


def contoh(nama):
    print(nama)


def todo_form(request):
    if request.method == 'GET':
        return render(request=request, template_name='todos/form_todo.html', context={
            'form': TodoModelForm(),
            'method': 'get'
        })
    else:
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request=request, template_name='todos/form_todo.html', context={
            'form': TodoForm(),
            'method': 'post'
        })


def todo_list(request):
    todos = Todo.objects.filter(title__contains='test')
    return render(request=request, template_name='todos/todo_list.html', context={
        'todos' : todos
    })

####


def hello(*args):
    for item in args:
        print(item)


