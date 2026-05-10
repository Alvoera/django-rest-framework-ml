
# Product Management API - Django REST Framework

Proyek ini adalah proyek latihan REST API sederhana untuk sistem manajemen produk yang dibangun menggunakan **Django** dan **Django REST Framework (DRF)**. API ini dirancang untuk menangani operasi CRUD (Create, Read, Update, Delete) pada data produk secara efisien.

## ✨ Fitur Utama

* **CRUD Otomatis**: Mendukung pengambilan daftar produk, pembuatan data baru, serta pembaruan dan penghapusan produk.
* **RESTful Architecture**: Menggunakan `ModelViewSet` dari DRF untuk standarisasi endpoint API.
* **Data Validation**: Serialisasi data otomatis menggunakan `ModelSerializer` untuk memastikan integritas data JSON.

## 📊 Struktur Data (Model)

Berdasarkan file `models.py`, setiap entitas **Product** memiliki atribut berikut:

* **Nama**: Nama produk (Teks, maksimal 255 karakter).
* **Deskripsi**: Penjelasan detail mengenai produk (Teks panjang).
* **Harga**: Nilai moneter produk (Format desimal).
* **Stok**: Jumlah ketersediaan produk (Bilangan bulat).
* **Waktu Dibuat**: Catatan waktu saat data produk pertama kali dimasukkan (Otomatis).

## 🚀 API Endpoints

API ini menyediakan endpoint standar berikut melalui `ProductViewSet`:

| Metode | Endpoint | Deskripsi |
| --- | --- | --- |
| **GET** | `/products/` | Mendapatkan semua daftar produk. |
| **POST** | `/products/` | Membuat data produk baru. |
| **GET** | `/products/{id}/` | Mendapatkan detail produk berdasarkan ID. |
| **PUT** | `/products/{id}/` | Memperbarui seluruh data produk. |
| **PATCH** | `/products/{id}/` | Memperbarui sebagian data produk. |
| **DELETE** | `/products/{id}/` | Menghapus data produk. |

## 🛠️ Teknologi & Library

* **Django**: Web framework utama.
* **Django REST Framework**: Untuk pembangunan API.
* **Python**: Bahasa pemrograman dasar.

## ⚙️ Cara Menjalankan

1. Pastikan Anda memiliki Django dan DRF terinstal:
```bash
pip install django djangorestframework

```


2. Jalankan migrasi untuk menyiapkan database:
```bash
python manage.py makemigrations
python manage.py migrate

```


3. Mulai server pengembangan:
```bash
python manage.py runserver

```


4. Akses API melalui `http://127.0.0.1:8000/`.

---

*Dokumentasi ini dibuat berdasarkan analisis terhadap file `models.py`, `serializers.py`, dan `views.py` dalam repositori ini.*
