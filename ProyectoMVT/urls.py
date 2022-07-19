from django.contrib import admin
from django.urls import path

from App_MVT.views import familia, lista_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/<nombre>/<edad>/<fecha_nacimiento>/', familia),
    path('lista_familiares/', lista_familiares),
]