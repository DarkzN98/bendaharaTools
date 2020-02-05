from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(default="", max_length=255)
    deskripsi_barang = models.TextField(default="")
    harga_barang = models.DecimalField(max_digits=10,decimal_places=3)
    qty_barang = models.IntegerField(default=1)
    tempat_beli_barang = models.ForeignKey('Toko', on_delete=models.CASCADE)
    pembeli_barang = models.ForeignKey('Pembeli', on_delete=models.CASCADE)
    tanggal_beli_barang = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.nama_barang} - {self.tempat_beli_barang}"

class Pembeli(models.Model):
    nama_pembeli = models.CharField(default="", max_length=255)
    
    def __str__(self):
        return self.nama_pembeli

class Toko(models.Model):
    nama_toko = models.CharField(default="", max_length=255)

    def __str__(self):
        return self.nama_toko