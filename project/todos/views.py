from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

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


####


def hello(*args):
    for item in args:
        print(item)


