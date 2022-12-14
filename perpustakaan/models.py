from django.db import models

# Create your models here.
class Kelompok(models.Model):
    nama=models.CharField(max_length=10)
    keterangan=models.TextField()

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul=models.CharField(max_length=50)
    penerbit=models.CharField(max_length=50)
    penulis=models.CharField(max_length=50)
    total=models.IntegerField(null=True)
    kelompok_id=models.ForeignKey(Kelompok,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.judul