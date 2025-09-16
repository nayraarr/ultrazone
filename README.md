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
Dalam pengimplementasian platform, data delivery berperan sebagai alat komunikasi antarpihak. Data delivery menentukan hasil dari proses manipulasi data nya dan apa yang akan ditampilkan oleh interfacenya. Misalnya, ketika pihak A perlu memfilter produk berdasarkan harganya. Pihak A akan meminta data product ke pihak B. Lalu, pihak B akan melakukan parsing data dalam format json kepada pihak A (data delivery). Barulah pihak A akan melakukan kalkulasi sebelum akhirnya dikirim ke interface user (data delivery). Data yang dikirim oleh pihak A juga menentukan apa yang dilihat oleh client.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, lebih baik menggunakan JSON tetapi kembali lagi pada kebutuhan masing" projek. Kelebihannya JSON adalah 
-Mudah untuk dibaca karena formatnya berupa pasangan key dan value seperti dictionary
-Hemat space karena format pertukarannya hanya membutuhkan sedikit memori dalam aplikasi
-Kompatibel karena banyak bahasa pemrograman, frameworks, os dan browser yang dapat menggunakan JSON secara langsung.
-Mandiri karena JSON tidak bergantung pada apapun untuk runtimenya.
-Fleksibel karena mendukung berbagai tipe data.
Sedangkan, XML adalah markup language dimana berisi kumpulan simbol yang dapat dibaca oleh manusia dan komputer. XML sebenarnya markup language yg dibuat untuk menyimpan data dan memfasilitasi pertukarannya dengan membuat sistem yg universal. XML bukanlah sebuah programming language karena tidak mengeksekusi algoritma dan tidak ada aturan yang mengikatnya. Fungsionalitas XML juga lebih luas dari JSON, xml mendukung lebih banyak tipe data.
Jadi, kembali pada kebutuhan masing" proyek. Jika membutuhkan tipe data kompleks, xml menyediakan fungsionalitasnya. Tetapi, jika data yang digunakan cukup standar, JSON menjadi opsi yang lebih baik ditambah formatnya yang lebih readable dibanding XML. Saya sendiri menyukai JSON karena bentuknya seperti dictionary.

Adapun, JSON lebih populer dikarenakan kecilnya ukuran file serta kecepatan transfer datanya. JSON bisa diparsing menggunakan js function. Sedangkan XML butuh diparsing menggunakan XML parser yang dimana lebih kompleks dan lambat. JSON juga menggunakan syntax yg minimum dan mudah dibaca. Sedangkan XML menggunakan struktur tag yang membuatnya semakin rumit. 

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() berperan memeriksa (memvalidasi) seluruh field/atribut yang dibutuhkan oleh form. Awalnya, method ini akan mengambil tiap atribut dari model form. Lalu, tiap atribut tadi diubah ke tipe data bawaan python . Tiap atribut divalidasi lewat batasan tipe datanya masing-masing. barulah divalidasi kembali dengan batasan atribut dari models bawaan nya. Jika ada error, simpan. Jika tidak ada error yang disimpan, return true. Tapi kalau ada error yang tersimpan, return false.
-> Kita membutuhkan method ini untuk memastikan data yang disimpan sudah sesuai format yang diinginkan. Dengan method ini, kita juga bisa memastikan data nya sudah bersih dan aman. Data yang disimpan tidak akan merusak database yang ada.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token adalah identifier/token unik bersamaan form kita yang dirender oleh user. Kita memerlukannya untuk melindungi aplikasi web dari serangan CSFR. Serangan ini membuat user melakukan sesuatu yang sebenarnya tidak ia inginkan. Ketika session user berjalan, django membuat token unik pada form yang di load user tersebut. Saat submisi, token ini dikirim secara bersamaan dengan jawaban user. Django akan memeriksa apakah token tersebut terdaftar pada user's cookie. Jika tidak, request submitnya ditolak. 
-> Jika tidak ditambahkan, attacker bisa membuat form palsu lalu submit sebagai user. Karena tidak ada validatornya, maka django akan memprosesnya tanpa tahu bahwa itu bukan user aslinya. Sehingga, attacker dapat memanipulasi data secara bebas. Attacker dapat mengubah pengaturan keamanan, mengambil data pribadi pada server, dll. 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Pada views.py direktori aplikasi main, saya membuat 4 function terlebih dahulu dengan 2 function menerima request client dan 2 functionnya lagi menerima request client beserta id.
-Pada fungsi show_xml, saya mengambil data seluruh product yang ada lalu di-serializers alias diubah ke bentuk xml. Setelah itu saya return http response bentuk xml tsb serta memberitahu browser client bahwa data yang diterima dalam format xml.
-Pada fungsi show_json, saya mengambil data seluruh product yang ada lalu di-serializers alias diubah ke bentuk JSON. Setelah itu saya return http response bentuk json tsb serta memberitahu browser client bahwa data yang diterima dalam format json.
-Pada fungsi show_xml_by_id, saya mengambil data product yang sesuai dengan id yang diberikan client. Data tsb lalu di-serializers alias diubah ke bentuk xml. Setelah itu saya return http response bentuk xml tsb serta memberitahu browser client bahwa data yang diterima dalam format xml.
-Pada fungsi show_json_by_id, saya mengambil data product yang sesuai dengan id. Data tsb lalu di-serializers alias diubah ke bentuk JSON. Setelah itu saya return http response bentuk json tsb serta memberitahu browser client bahwa data yang diterima dalam format json.
2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
Karena fungsi di views.py sudah ada, pada urls.py ditambahkanlah path yang bersesuaian dengan fungsi yang dibuat tadi dengan memasukkan kode berikut.
`...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
...`
3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
-Pada halaman utama, agar menampilkan seluruh data objek model yang sudah ada, cukup tambahkan placeholder pada main.html nya dan sesuaikan tampilan yang diinginkannya. Nanti, main.html akan me-looping seluruh objeknya dan menampilkannya.
-Untuk menambah tombol 'add', pada main.html utama cukup tambahkan anchortag(hyperlink) yang membungkus button add. Arahakan hyperlink tsb pada fungsi create_product yang terdapat di main. Berikut adalah kode yang digunakan,
`<a href="{% url 'main:create_product' %}">
  <button>+ Add Product</button>
</a>`
di create_product barulah pembuatan form dilakukan dengan merender create_product.html. Setelah mengirim data dan valid, barulah django akan kembali ke halaman utamanya (show_main). 
-Untuk menambahkan tombol detail, pada main.html utama cukup tambahkan anchortag(hyperlink) yang membungkus button add. Arahakan hyperlink tsb pada fungsi show_product yang terdapat di main, serta kirimkan id product yang sedang dilihat detailnya. Berikut adalah kode yang digunakan,
`<a href="{% url 'main:show_product' product.id %}">
    <button>View Details</button>
</a>`
di show_product, produk tersebut akan dicari berdasarkan id. Lalu template show_product.html akan dirender dengan mengganti placeholder informasi dengan produk yang sudah diambil tadi.

4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
Pembuatannya cukup menggunakan class dari django itu sendiri di forms.py. Dengan import ModelForm dari django forms, kita bisa membuat child dari modelForm itu sendiri berupa productForm. Pada class ini, dengan mendefinisikan
`model = Product
fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'brand']`
, kita sama saja memberi tahu django untuk membuat form yang bersesuaian dengan model Product. Nantinya, form akan menampilkan data yang ada di variabel fields. 
Setelah membuat ModelForm, pada templatenya kita hanya perlu memakai fasilitas yang disediakan django. Dengan command,
`{{ form.as_table }}`
maka django forms yang kita buat tadi akan otomatis dibuat tampilannya.
5. Membuat halaman yang menampilkan detail dari setiap data objek model.
di fungsi show_product, akan merender template show_product.html. Di file html itulah dibuat placeholder untuk tiap atribut dari productnya.
`<h1>{{ product.name }}</h1>
<p><b>{{ product.get_category_display }}</b>
    {% if product.is_featured %} | 
    <b>Featured</b>
    {% endif %}
    | Brand: {{ product.brand }}
    | Rating: {{ product.rating }} 
    | Price: Rp {{ product.price }}
</p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="News thumbnail" width="300">
<br /><br />
{% endif %}`

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada.

### Tautan hasil akses url pada Postman
LINK : https://drive.google.com/drive/folders/1yy0W2ZkXW19boZpuxNJyBtv_kIFqgDZ2?usp=sharing
