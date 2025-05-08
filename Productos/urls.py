from django.contrib import admin
from django.urls import path, include
from . import views

## INSTRU NO VUELVA A PEDIR TRUCHA EN LA VIDA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agregar/', views.agregar, name='agregar'),
    path('actualizar/<int:id_prod>', views.actualizar, name='actualizar'),
    path('eliminar/<int:id_prod>', views.eliminar, name='eliminar')
]
