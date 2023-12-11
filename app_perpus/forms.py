from django import forms
from .models import Kategori,Buku, Anggota, Peminjaman, Petugas

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = "__all__"
class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = "__all__"
class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = "__all__"
class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        fields = "__all__"
class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = "__all__"

