from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku,penerbit,main,tambah_buku   



urlpatterns = [
    path('',main),
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/',penerbit),
    path('tambah/',tambah_buku),
    
]
 