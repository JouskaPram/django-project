
from django.forms import ModelForm
from .models import Buku
from django import forms

class FormBuku(ModelForm):
    class Meta:
        model=Buku
        fields = "__all__"


        widgets={
            'judul':forms.TextInput({
                'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
                }),
            'penulis':forms.TextInput({
                'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
                }),
            'penerbit':forms.TextInput({
                'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
                }),
            'total':forms.NumberInput({
                'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
                }),
            
        }