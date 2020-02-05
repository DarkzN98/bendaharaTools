from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Barang

# Create your views here.
def index(Request):
    barang_list = Barang.objects.order_by('tanggal_beli_barang')
    template = loader.get_template('uangbulanan/index.html')
    context = {
        'barang_list': barang_list
    }
    return HttpResponse(template.render(context, Request))

def get_barang_bulan_ini(Request):
    barang_list = Barang.objects.filter(tanggal_beli_barang__month=timezone.now().month)
    template = loader.get_template('uangbulanan/index.html')
    context = {
        'barang_list': barang_list
    }
    return HttpResponse(template.render(context, Request))

def insert_barang_page(Request):
    template = loader.get_template('uangbulanan/insert.html')
    context = {}
    return HttpResponse(template.render(context, Request))