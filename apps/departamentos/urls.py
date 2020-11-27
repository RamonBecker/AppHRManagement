from django.urls import path, include
from .views import DepartamentosList, DepartamentoCreate

urlpatterns = [
    path('lista', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),

]
