from django.contrib import admin
from .models import Kategori, Buku, Anggota, Petugas, Peminjaman

# Register your models here.
admin.site.register(Kategori)
admin.site.register(Buku)
admin.site.register(Anggota)
admin.site.register(Peminjaman)
admin.site.register(Petugas)

