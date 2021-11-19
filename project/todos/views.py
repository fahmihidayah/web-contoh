from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('hallo fahmi')


def penjumlahan(request, angka1, angka2):
    total = angka1 + angka2
    return HttpResponse('Hasil adalah ' + str(total))


def contoh_html(req):
    contoh(nama='fahmi')
    return render(request=req, template_name='hello.html')


def contoh(nama):
    print(nama)