from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tablas', tablas, name='tablas'),
    path('updateEmpleado/<int:pk_employee>', updateEmpleado, name="updateEmpleado"),
    path('deleteEmpleado/<int:pk_employee>', deleteEmpleado, name="deleteEmpleado"),

]