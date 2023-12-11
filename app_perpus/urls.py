from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignupPage, name='signup'),
    path('signin/', views.SigninPage, name='signin'),
    path('signout/', views.SignoutPage, name='signout'),

    # Kategori
    path('kategori/', views.list_kategori, name='list_kategori'),
    path('kategori/create/', views.create_kategori, name='create_kategori'),
    path('kategori/update/<int:kategori_id>/', views.update_kategori, name='update_kategori'),
    path('kategori/delete/<int:kategori_id>/', views.delete_kategori, name='delete_kategori'),

    # Buku
    path('buku/', views.list_buku, name='list_buku'),
    path('buku/create/', views.create_buku, name='create_buku'),
    path('buku/update/<int:buku_id>/', views.update_buku, name='update_buku'),
    path('buku/delete/<int:buku_id>/', views.delete_buku, name='delete_buku'),

    # Anggota
    path('anggota/', views.list_anggota, name='list_anggota'),
    path('anggota/create/', views.create_anggota, name='create_anggota'),
    path('anggota/update/<int:anggota_id>/', views.update_anggota, name='update_anggota'),
    path('anggota/delete/<int:anggota_id>/', views.delete_anggota, name='delete_anggota'),

    # Peminjaman
    path('peminjaman/', views.list_peminjaman, name='list_peminjaman'),
    path('peminjaman/create/', views.create_peminjaman, name='create_peminjaman'),
    path('peminjaman/update/<int:peminjaman_id>/', views.update_peminjaman, name='update_peminjaman'),
    path('peminjaman/delete/<int:peminjaman_id>/', views.delete_peminjaman, name='delete_peminjaman'),

    # Petugas
    path('petugas/', views.list_petugas, name='list_petugas'),
    path('petugas/create/', views.create_petugas, name='create_petugas'),
    path('petugas/update/<int:petugas_id>/', views.update_petugas, name='update_petugas'),
    path('petugas/delete/<int:petugas_id>/', views.delete_petugas, name='delete_petugas'),
]
