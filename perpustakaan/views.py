from django.shortcuts import render
from perpustakaan.models import Buku
from .forms import FormBuku

def buku(request):
    books = Buku.objects.all()
    konteks={
       'books': books,
    }
    return render(request,'buku.html',konteks)
def penerbit(request):
    return render(request,'penerbit.html')

def main(request):
    return render(request,'main.html')

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form=FormBuku()
            pesan="data sukses di simpan"
            konteks={
                'form':form,
                'pesan':pesan, 
            }
            return render(request,'tambah-buku.html',konteks)
    else:   
        form = FormBuku()


        konteks={
          'form':form,
        }

    return render(request,'tambah-buku.html',konteks)
