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

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control','style':'height: 20px;'}),
            'penulis': forms.TextInput(attrs={'class': 'form-control'}),
            'tahun_terbit': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
        }
        
class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = "__all__"
        
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control','style':'height: 20px;'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom email validation if necessary
        return email

    def clean_nomor_telepon(self):
        nomor_telepon = self.cleaned_data.get('nomor_telepon')
        # Add custom phone number validation if necessary
        return nomor_telepon
    
class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        fields = "__all__"
class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = "__all__"

        widgets = {
            'buku': forms.Select(attrs={'class': 'form-control'}),
            'anggota': forms.Select(attrs={'class': 'form-control'}),
            'tanggal_peminjaman': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'tanggal_pengembalian': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

