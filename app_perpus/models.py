from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='buku_set')

    def __str__(self):
        return self.judul


class Anggota(models.Model):
    foto = models.ImageField(upload_to='img', default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='anggota')
    KELAMIN_CHOICES = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    kelamin = models.CharField(max_length=10, choices=KELAMIN_CHOICES)
    alamat = models.CharField(max_length=200)
    email = models.CharField(max_length=20, default='anggota@gmail.com')
    nomor_telepon = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    STATUS_CHOICES = [
        ('pinjam', 'Dipinjam'),
        ('kembali', 'Dikembalikan'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.anggota.user.username} - {self.buku.judul}"

    def is_kembali(self):
        return self.tanggal_pengembalian < timezone.now() and self.status == 'pinjam'


class Petugas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='petugas')
    posisi = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def is_staff(self):
        return self.user.is_staff
