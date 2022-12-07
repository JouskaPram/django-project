from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',main),
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/',penerbit),
    path('tambah/',tambah_buku),
    path('buku/ubah/<int:id_buku>',ubah_buku,name="ubah_buku"),
    path('buku/delete/<int:id_buku>',delete_buku,name="delete_buku"),
    path('login/',LoginView.as_view(),name="login"),
]
 