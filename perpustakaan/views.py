from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from .forms import FormBuku
from django.contrib import messages



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
def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = "ubah-buku.html"
    if request.POST:
        form = FormBuku(request.POST,instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,"data berhasil di ubah")
            return redirect('ubah_buku',id_buku=id_buku)

    else:
        form = FormBuku(instance=buku)
        konteks ={
            'form':form,
            'buku':buku,
        }

    return render(request,template,konteks)
