from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(default="", max_length=255)
    deskripsi_barang = models.TextField(default="")
    harga_barang = models.DecimalField(max_digits=10,decimal_places=3)
    qty_barang = models.IntegerField(default=1)
    tempat_beli_barang = models.CharField(default="", max_length=255)
    pembeli_barang = models.CharField(default="", max_length=255)
    tanggal_beli_barang = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.nama_barang} - {self.tempat_beli_barang}"