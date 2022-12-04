from django.contrib import admin
from django.urls import path
from perpustakaan.views import *



urlpatterns = [
    path('',main),
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/',penerbit),
    path('tambah/',tambah_buku),
    path('buku/ubah/<int:id_buku>',ubah_buku,name="ubah_buku")
    
]
 