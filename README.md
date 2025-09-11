Nama : Zita Nayra Ardini
NPM : 2406404913
Kelas : PBP - F

# Tugas 2
### Tautan PWS Deploy
https://zita-nayra-ultrazone.pbp.cs.ui.ac.id

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-> setiap langkah tentunya termasuk remote serta commit dan push ke direktori github. 
1. Membuat sebuah proyek Django baru.
: Awalnya, saya membuat set up project nya dulu, dimulai dari membuat repositori git kosong lalu meng-install seluruh requirements projek. Setelah itu, saya membuat environment beserta projek django baru dengan menjalankan perintah 
'django-admin startproject <NAMA_PROJECT> .'
serta membuat konfigurasi settings.py, .env, .env.prod, serta gitignore nya.
2. Membuat aplikasi dengan nama main pada proyek tersebut.
Lalu saya menjalankan perintah
'python manage.py startapp <NAMA_APLIKASI>'
untuk membuat aplikasi baru dan mendaftarkannya ke INSTALLED_APPS di settings.py. 
Saya membuat 1 file html juga sebagai template awal aplikasi lalu menggunakannya di views.py direktori aplikasi dan mendaftarkannya di urls.py direktori aplikasi. 
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Untuk menjalankan aplikasi main, saya mendaftarkan/memasukkan path yang ada di urls.py direktori aplikasi ke urls.py direktori projek dengan menambahkan perintah
path('', include('main.urls')). Sehingga, url yang ada di aplikasi saat ini bisa dijalankan oleh projek.
4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
Pada models.py direktori projek, saya mengimpor 'models' dari library django.db. Saya membuat model bernama product yang berisi atribut" yang sudah ditentukan dan tambahannya. Tiap atribut memiliki tipe data yang berbeda ketentuannya.
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Pada views.py direktori projek, saya membuat function 'show_main' yang berisi data diri saya dalam bentuk dictionary. Setelah itu, saya mengganti variabel pada template yang akan digunakan menjadi variabel placeholder. Sehingga saat 'show_main' dijalankan maka akan merender template html dengan data yang berisi dictionary yang sudah saya definisikan sebelumnya.
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Pada urls.py direktori aplikasi, saya mengimport method show_main yang terdapat pada views.py direktori aplikasi. Hal ini membuat jika client mengakses path '', maka urls.py akan menjalankan/mengeksekusi show_main yang terdapat di views.py. Oleh karena itu akhirnya template html akan terender. 
Setelah itu, saya melakukan migrate pada perubahan struktur data di models.py. Setelah di push ke direktori github, saya membuat projek baru di website pws. Saya menyalin kredensial serta menambahkan variabel environment nya. Lalu saya menambahkan url deploynya ke ALLOWED_HOST pada settings.py direktori projek. Stelah itu saya push ke pws nya dan web nya sudah bisa diakses secara online.  

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
LINK: https://drive.google.com/file/d/12yf9i5sBMxEnXsC7ZrIuzEgJDB2wzd1G/view?usp=sharing
>> Kaitan
urls.py akan mengarahkan request client ke function yang sesuai di views.py. Setelah itu, request client akan diproses di function tsb. Ketika membutuhkan manipulasi data (menambah, mengurangi, mengubah, dll), views.py akan mengakses models.py yang berisi struktur data yang didefinisikan di database. Setelah pemrosesan data selesai, views.py akan mengambil template tampilan yang sesuai berupa berkas html. Views.py akan merender berkas html disesuaikan dengan data yang telah diproses (mereplace). Setelah itu barulah views.py mengembalikan ke client.

### Jelaskan peran settings.py dalam proyek Django!
Settings.py pada django berisi seluruh konfigurasi pada django projek yang sedang dikerjakan. Pada dasarnya file ini berisi modul python beserta variabel modul nya.Setiap variabelnya ditulis dalam bentuk kapital. Beberapa variabel yang ada diantaranya,
'BASE_DIR' untuk menunjuk direktori utama projek (path lain relatif thp utama), 'DEBUG' untuk menampilkan/tidaknya bagian error yang dialami, 'ALLOWED_HOST' untuk mendaftarkan domain yang boleh mengakses projek, 'INSTALLED_APPS' untuk mengaktifkan aplikasi (fitur) projek, dan masih banyak lagi.

### Bagaimana cara kerja migrasi database di Django?
Migrasi dalam django artinya menerapkan perubahan bentuk model ke database yang kita miliki. Di Django, setiap model yang akan diterapkan ke database akan menghasilkan file migrasinya. File ini berisi apa saja yang ada pada struktur database, termasuk menambahkan tabel baru, menghapus kolom, atau merubah tipe data. Cara kerja migrasi data:
1. Membuat model data di models.py
2. Lakukan perintah 'makemigrations', lalu django akan merepresentasikan perubahan model dalam bentuk file migrasi. Ini sama saja seperti nge-list bentuk/perubahan struktur apa yang ingin diterapkan pada database.
3. Menerapkan 'migrasi' pada databse. Django secara otomatis akan membuat struktur tabel sesuai dengan apa yang ada di file migrasi sebelumnya (menerapkan struktur yang sudah di-list di file migrasi). Django akan CREATE TABLE, ADD COLUMN, dll secara otomatis sehingga membentuk struktur database terbaru. 

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, django dijadikan permulaan pembelajaraan pemrograman platfrom dikarenakan bahasa pengantarnya adalah python. Mahasiswa Fasilkom umumnya sudah familiar dengan bahasa ini sehingga dalam pembelajarannya hanya perlu memahami konsep/alur memprogram platformnya saja. Selain itu, kerangka kerja django juga terorganisir dengan baik dan mudah diterapkan. Kerangka kerja django sudah menyediakan fitur siap pakai untuk beberapa tugas pengembang web umum. Karena memiliki ORM (Object Relational Mapping) bawaan, django memungkinkan kita untuk mengembangkan database tanpa menulis query SQL nya. Hanya perlu mendefinisikan model di models.py, django otomatis membuat tabel database dan method query nya. Routing di django juga cukup sederhana. Kita hanya perlu mendefinisikannya di urls.py, lalu membuat fungsi untuk menghubungkannya di view. Django juga  sudah memiliki perlindungan bawaan terhadap kebanyakan jenis serangan cyber sehingga aman digunakan. Django memiliki komunitas yang besar dan aktif, dokumentasi nya juga lengkap dan terperinci. 

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
tidak ada, asisten dosen sangat membantu.

# Tugas 3
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
### Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?