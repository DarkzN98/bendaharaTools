# Generated by Django 3.0.2 on 2020-02-05 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uangbulanan', '0002_auto_20200130_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pembeli', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_toko', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='barang',
            name='pembeli_barang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uangbulanan.Pembeli'),
        ),
        migrations.AlterField(
            model_name='barang',
            name='tempat_beli_barang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uangbulanan.Toko'),
        ),
    ]
