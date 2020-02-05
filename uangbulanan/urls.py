from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_barang_bulan_ini, name='get_barang_bulan_ini'),
    path('dashboard', views.get_barang_bulan_ini, name='dashboard'),
    path('insert', views.insert_barang_page, name='insert'),
]