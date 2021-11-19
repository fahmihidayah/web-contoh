from django.urls import path

from .views import index, penjumlahan, contoh_html


urlpatterns = [
    path('hello_index', index, name='hello_index'),
    path('penjumlahan/<int:angka1>/<int:angka2>', penjumlahan, name='pejumlahan'),
    path('coba_template', contoh_html, name='contoh_html')
]