from django.contrib import admin
from .models import Barang, Pembeli, Toko

# Register your models here.
admin.site.register(Barang)
admin.site.register(Pembeli)
admin.site.register(Toko)