from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

from django.views.generic import TemplateView

from .forms import TodoForm, TodoModelForm
from .models import Todo

from django.views.decorators.csrf import csrf_exempt

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

## CREATE
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
        return redirect('todo_list')
        # return render(request=request, template_name='todos/form_todo.html', context={
        #     'form': TodoForm(),
        #     'method': 'post'
        # })

## READ
def todo_list(request):
    todos = Todo.objects.all()
    return render(request=request, template_name='todos/list.html', context={
        'todos' : todos
    })

## UPDATE
def update_todo(request, **kwargs):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=kwargs['pk'])
        form = TodoModelForm(instance=todo)
        return render(request=request, template_name='todos/form_todo.html', context={'form': form})
    else:
        todo = Todo.objects.get(pk=kwargs['pk'])
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo_list')

## DELETE
def delete_todo(request, **kwargs):
    if request.method == 'POST':
        todos = Todo.objects.get(pk=kwargs['pk'])
        todos.delete()
        return redirect('todo_list')

def list_test(request):

    todos = Todo.objects.all()

    return render(request=request, template_name='todos/list.html', context= {'list' : todos})


@csrf_exempt
def list_todo_api(request):
    # ini kembaliannya QUERY set dimana bisa di lakukan query lagi setelah nya
    # Todo.objects.all().filter(title__contains=123123)
    # ini kembaliannya actual data, artinya dia tidak bisa di query lagi
    todo = Todo.objects.values('id', 'title', 'description')
    return JsonResponse({'data' : list(todo)})



####


def hello(*args):
    for item in args:
        print(item)


