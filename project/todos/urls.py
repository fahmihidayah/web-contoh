from django.urls import path

from .views import index, penjumlahan, contoh_html, IndexCoba, todo_form, todo_list, list_test, delete_todo, update_todo, list_todo_api


urlpatterns = [
    path('hello_index', index, name='hello_index'),
    path('penjumlahan/<int:angka1>/<int:angka2>', penjumlahan, name='pejumlahan'),
    path('coba_template', contoh_html, name='contoh_html'),
    path('template_view_sample', IndexCoba.as_view(), name='template_view_sample'),
    path('form_todo', todo_form, name='form_todo'),
    path('todo_list', todo_list, name='todo_list'),
    path('todo_delete/<int:pk>', delete_todo, name='delete_todo'),
    path('update_todo/<int:pk>', update_todo, name='update_todo'),

    path('api/todos', list_todo_api, name='list_todo_api'),

    path('list_test', list_test, name='list_test'),
]