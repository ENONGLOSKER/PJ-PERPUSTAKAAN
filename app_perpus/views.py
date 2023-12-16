from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404
from datetime import date
from django.utils import timezone
from .models import Anggota, Kategori, Petugas, Buku, User,Peminjaman
from .forms import KategoriForm, BukuForm, AnggotaForm, PeminjamanForm, PetugasForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# ANGGOTA
# Fungsi untuk menampilkan Anggota 
@login_required
def list_anggota(request):
    anggotas = Anggota.objects.all()
    search_query = request.GET.get('cari')

    if search_query:
        anggota_serc = Anggota.objects.filter(
            Q(user__username__icontains=search_query) | Q(alamat__icontains=search_query)
        )
    else:
        anggota_serc = anggotas
    
    paginator = Paginator(anggota_serc, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user = User.objects.all()
    recent_anggotas = Anggota.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).order_by('-id')[:5]
    context = {
        'recent_anggotas': recent_anggotas,
        'anggotas': page_obj,
        'user': user,
    }
    return render(request, 'anggota.html', context)

# Fungsi untuk menambahkan anggota baru
@login_required
def create_anggota(request):
    if request.method == 'POST':
        form = AnggotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_anggota')
    else:
        form = AnggotaForm()

    return render(request, 'anggota_add.html', {'form': form})

# Fungsi untuk memperbarui anggota
@login_required
def update_anggota(request, anggota_id):
    anggota = get_object_or_404(Anggota, id=anggota_id)

    if request.method == 'POST':
        form = AnggotaForm(request.POST, request.FILES, instance=anggota)
        if form.is_valid():
            form.save()
            return redirect('list_anggota') 
    else:
        form = AnggotaForm(instance=anggota)

    return render(request, 'anggota_add.html', {'form': form, 'anggota': anggota})

# Fungsi untuk menghapus anggota
@login_required
def delete_anggota(request, anggota_id):
    anggota = get_object_or_404(Anggota, pk=anggota_id)
    anggota.delete()
    return redirect('list_anggota')


# KATERGORI
@login_required
def list_kategori(request):
    kategoris = Kategori.objects.all()
    return render(request, 'kategori.html', {'kategoris': kategoris})

# Fungsi untuk menambahkan kategori baru
@login_required
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
@login_required
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
@login_required
def delete_kategori(request, kategori_id):
    kategori = get_object_or_404(Kategori, pk=kategori_id)
    kategori.delete()
    return redirect('list_kategori')


# BUKU
# Fungsi untuk menambahkan buku baru
@login_required
def list_buku(request):
    bukus = Buku.objects.all()
    search_query = request.GET.get('cari')

    if search_query:
        buku_serc = Buku.objects.filter( Q(judul__icontains=search_query) | Q(kategori__nama_kategori = search_query))
    else:
        buku_serc = bukus
    
    paginator = Paginator(buku_serc, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    kategoris = Kategori.objects.all()
    context = {
        'bukus':page_obj,
        'kategoris':kategoris,
    }
    return render(request, 'buku.html', context)

@login_required
def create_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_buku')
    else:
        form = BukuForm()
    return render(request, 'buku_add.html', {'form': form})

# Fungsi untuk memperbarui buku
@login_required
def update_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('list_buku')
    else:
        form = BukuForm(instance=buku)
    return render(request, 'buku_add.html', {'form': form, 'buku': buku})

# Fungsi untuk menghapus buku
@login_required
def delete_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    buku.delete()
    return redirect('list_buku')


# PINJAMAN
# Fungsi untuk menambahkan peminjaman baru
@login_required
def list_peminjaman(request):
    peminjamans = Peminjaman.objects.all()
    search_query = request.GET.get('cari')

    if search_query:
        peminjam = Peminjaman.objects.filter(Q(buku__judul__icontains=search_query) | Q(anggota__icontains=search_query)|Q(status__icontains=search_query)|Q(tanggal_peminjaman__icontains=search_query)|Q(tanggal_pengembalian__icontains=search_query))
    else:
        peminjams = peminjamans
    
    paginator = Paginator(peminjams,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    status_pinjam = Peminjaman.objects.filter(status='pinjam').order_by('-id')

    context = {
        'peminjamans': peminjamans,
        'peminjams':page_obj,
        'status_pinjam':status_pinjam,
        }
    return render(request, 'peminjam.html', context)

# Fungsi untuk menambahkan peminjaman baru
@login_required
def create_peminjaman(request):
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_peminjaman')
    else:
        form = PeminjamanForm()
    return render(request, 'peminjaman_add.html', {'form': form})

# Fungsi untuk memperbarui peminjaman
@login_required
def update_peminjaman(request, peminjaman_id):
    peminjaman = get_object_or_404(Peminjaman, pk=peminjaman_id)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, instance=peminjaman)
        if form.is_valid():
            form.save()
            return redirect('list_peminjaman')
    else:
        form = PeminjamanForm(instance=peminjaman)
    return render(request, 'peminjaman_add.html', {'form': form, 'peminjaman': peminjaman})

# Fungsi untuk menghapus peminjaman
@login_required
def delete_peminjaman(request, peminjaman_id):
    peminjaman = get_object_or_404(Peminjaman, pk=peminjaman_id)
    peminjaman.delete()
    return redirect('list_peminjaman')


# PETUGAS
# Fungsi untuk menambahkan petugas baru
@login_required
def list_petugas(request):
    petugass = Petugas.objects.all()
    return render(request, 'petugas.html', {'petugass': petugass})

# Fungsi untuk menambahkan petugas baru
@login_required
def create_petugas(request):
    if request.method == 'POST':
        form = PetugasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_petugas')
    else:
        form = PetugasForm()
    return render(request, 'create_petugas.html', {'form': form})

# Fungsi untuk memperbarui petugas
@login_required
def update_petugas(request, petugas_id):
    petugas = get_object_or_404(petugas, pk=petugas_id)
    if request.method == 'POST':
        form = PetugasForm(request.POST, instance=petugas)
        if form.is_valid():
            form.save()
            return redirect('list_petugas')
    else:
        form = PetugasForm(instance=petugas)
    return render(request, 'update_petugas.html', {'form': form, 'petugas': petugas})

# Fungsi untuk menghapus petugas
@login_required
def delete_petugas(request, petugas_id):
    petugas = get_object_or_404(petugas, pk=petugas_id)
    petugas.delete()
    return redirect('list_petugas')

def index(request):
    return render(request, 'index.html')
@login_required
def dashboard(request):
    anggotas = Anggota.objects.all().order_by('-id')[:5]
    anggota = Anggota.objects.all().count()
    buku = Buku.objects.all().count()
    kategori = Kategori.objects.all().count()
    peminjam = Peminjaman.objects.all().count()
    context= {
        'anggota':anggotas,
        'jlh_anggota':anggota,
        'jlh_buku':buku,
        'jlh_kategori':kategori,
        'jlh_peminjam':peminjam,
        }
    return render(request, 'dashboard.html',context)

def SigninPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('dashboard')
        else:
            return redirect('signin')
    return render(request, 'signin.html')

def SignoutPage(request):
    logout(request)
    return redirect('index')

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
            return redirect('signin')

    return render(request, 'signup.html')
 
