from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404
from datetime import date
from . models import Anggota, Kategori, Petugas, Buku
from .forms import KategoriForm 


# Create your views here.
def index(request):
    return render(request, 'dashboard.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Password tidak sama!")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)

            # Menambahkan pengguna ke grup 'tamu' atau mendapatkan grup jika belum ada
            group, created = Group.objects.get_or_create(name='tamu')
            my_user.groups.add(group)

            # Menambahkan izin 'view_user' ke pengguna
            permission = Permission.objects.get(codename='view_user')
            my_user.user_permissions.add(permission)

            my_user.save()
            messages.success(request, "Selamat, Register Berhasil!")
            return redirect('/')

    return render(request, 'signup.html')


# KATERGORI
def list_kategori(request):
    kategoris = read_kategori()
    return render(request, 'list_kategori.html', {'kategoris': kategoris})

# Fungsi untuk menambahkan kategori baru
def create_kategori(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_kategori')
    else:
        form = KategoriForm()
    return render(request, 'create_kategori.html', {'form': form})

# Fungsi untuk memperbarui kategori
def update_kategori(request, kategori_id):
    kategori = get_object_or_404(Kategori, pk=kategori_id)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('list_kategori')
    else:
        form = KategoriForm(instance=kategori)
    return render(request, 'update_kategori.html', {'form': form, 'kategori': kategori})

# Fungsi untuk menghapus kategori
def delete_kategori(request, kategori_id):
    kategori = get_object_or_404(Kategori, pk=kategori_id)
    kategori.delete()
    return redirect('list_kategori')


# BUKU
# Fungsi untuk menambahkan buku baru
def create_buku(judul, penulis, tahun_terbit, kategori_id):
    kategori = get_object_or_404(Kategori, pk=kategori_id)
    return Buku.objects.create(judul=judul, penulis=penulis, tahun_terbit=tahun_terbit, kategori=kategori)

# Fungsi untuk membaca (menampilkan) semua buku
def read_buku():
    return Buku.objects.all()

# Fungsi untuk memperbarui informasi buku
def update_buku(buku_id, judul_baru, penulis_baru, tahun_terbit_baru, kategori_id_baru):
    buku = get_object_or_404(Buku, pk=buku_id)
    kategori_baru = get_object_or_404(Kategori, pk=kategori_id_baru)
    
    buku.judul = judul_baru
    buku.penulis = penulis_baru
    buku.tahun_terbit = tahun_terbit_baru
    buku.kategori = kategori_baru
    
    buku.save()

# Fungsi untuk menghapus buku
def delete_buku(buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    buku.delete()


# ANGGOTA
# Fungsi untuk menambahkan anggota baru
def create_anggota(username, password, alamat, nomor_telepon):
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    
    anggota = Anggota.objects.create(user=user, alamat=alamat, nomor_telepon=nomor_telepon)
    return anggota

# Fungsi untuk membaca (menampilkan) semua anggota
def read_anggota(request):
    data = Anggota.objects.all()
    return render(request,'anggota.html')

# Fungsi untuk memperbarui informasi anggota
def update_anggota(anggota_id, alamat_baru, nomor_telepon_baru):
    anggota = get_object_or_404(Anggota, pk=anggota_id)
    
    anggota.alamat = alamat_baru
    anggota.nomor_telepon = nomor_telepon_baru
    
    anggota.save()

# Fungsi untuk menghapus anggota
def delete_anggota(anggota_id):
    anggota = get_object_or_404(Anggota, pk=anggota_id)
    anggota.delete()


# PINJAMAN
# Fungsi untuk menambahkan peminjaman buku
def create_peminjaman(buku_id, anggota_id, tanggal_peminjaman, tanggal_pengembalian, status):
    buku = get_object_or_404(Buku, pk=buku_id)
    anggota = get_object_or_404(Anggota, pk=anggota_id)
    
    return Peminjaman.objects.create(
        buku=buku,
        anggota=anggota,
        tanggal_peminjaman=tanggal_peminjaman,
        tanggal_pengembalian=tanggal_pengembalian,
        status=status
    )

# Fungsi untuk membaca (menampilkan) semua peminjaman
def read_peminjaman():
    return Peminjaman.objects.all()

# Fungsi untuk memperbarui informasi peminjaman
def update_peminjaman(peminjaman_id, tanggal_pengembalian_baru, status_baru):
    peminjaman = get_object_or_404(Peminjaman, pk=peminjaman_id)
    
    peminjaman.tanggal_pengembalian = tanggal_pengembalian_baru
    peminjaman.status = status_baru
    
    peminjaman.save()

# Fungsi untuk menghapus peminjaman
def delete_peminjaman(peminjaman_id):
    peminjaman = get_object_or_404(Peminjaman, pk=peminjaman_id)
    peminjaman.delete()


# PETUGAS
# Fungsi untuk menambahkan petugas baru
def create_petugas(username, password, posisi):
    user = User.objects.create(username=username, is_staff=True)
    user.set_password(password)
    user.save()
    
    petugas = Petugas.objects.create(user=user, posisi=posisi)
    return petugas

# Fungsi untuk membaca (menampilkan) semua petugas
def read_petugas():
    return Petugas.objects.all()

# Fungsi untuk memperbarui informasi petugas
def update_petugas(petugas_id, posisi_baru):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    
    petugas.posisi = posisi_baru
    
    petugas.save()

# Fungsi untuk menghapus petugas
def delete_petugas(petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    petugas.delete()
