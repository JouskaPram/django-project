from django.contrib import admin
from perpustakaan.models import Buku,Kelompok
# Register your models here.
class BukuAdmin(admin.ModelAdmin):
        list_display=['judul','penulis','kelompok_id','total']
        search_fields=['judul','penulis']
        list_per_page=3
        list_filter=['kelompok_id']      
        
        
admin.site.register(Buku,BukuAdmin)
admin.site.register(Kelompok)