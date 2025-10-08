Nama : Zita Nayra Ardini
NPM : 2406404913
Kelas : PBP - F

### Tautan PWS Deploy
https://zita-nayra-ultrazone.pbp.cs.ui.ac.id

### Tautan PWS Deploy

<details>
<summary>Tugas Individu 2</summary>

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
</details>

<details>
<summary>Tugas Individu 3</summary>
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

</details>

<details>
<summary>Tugas Individu 4</summary>

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah formulir bawaan jango untuk mengautentikasi/memverifikasi identitas pengguna. Dalam pembuatannya, kita tidak perlu susah payah kembali membuat fieldnya satu", hanya cukup menggunakan bawaan django saja. Kelebihannya, dapat meningkatkan keamanan (tidak akan ada akses tidak sah), serta dapat menghindari pencurian identitas dan penyalahgunaan data pribadi. Kekurangannya, syarat password yang cukup rumit,  rentan phising dan malware, 

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi merupakan cara django untuk memverifikasi/memeriksa identitas user yang sedang login, apakah user ada di database, apakah passwordnya sesuai, dll. Sedngkan, otorisasi adalah cara django memeriksa apa saja hal yang dapat dilakukan oleh user tersebut. Pengaplikasiannya dilakukan ketika user login (pada method login_user di views.py), akan dibuat sebuah authentication form. Form ini memeriksa data yang kita kirim, misalnya apakah nama ada di database atau kredensialnya aman. Kita tidak perlu mendefinisikannya logic nya masing masing lagi karena sudah disediakan oleh django. karena otorisasi memeriksa hak akses,
Django mencari dulu permission yang terdapat di user saat ini. Jika terdaftar, maka request akan dilanjutkan sesuai keinginan user. Jika tidak, django akan mengembalikan kode 403 (redirect ke login).

### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
-Kelebihannya adalah data lebih susah dimodifikasi/dicuri karena data disimpan di session pada server. Cookie bisa dibuat menjadi persistent/bertahan antar sesi, sehingga client tidak perlu ke default website lagi setiap kali mengaksesnya. Cookie dapat meringankan beban server dengan membawa data yang tidak sensitif sehingga storage server tidak penuh dan berisi informasi penting saja. Server juga memiliki kekuasaan penuh atas data yang disimpan dan klien juga bebas mengatur cookienya.
-Kekurangannya, karena data pada cookie ada pada client, rentan terkena searngan XSS. Jika tidak waspada, data bisa diubah"/dicuri. Keamanan dari cookie sendiri bergantung pada settingan awal nya juga. Session dan cookie juga tidak cocok untuk data besar, pengiriman cookie dengan isi yang besar dapat membuat cookie terpaksa dipotong untuk dapat dikirim dan juga server tentunya membutuhkan storage yang lebih besar. Jika space kurang, hal ini dapat memperlambat proses yang ada pada server.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Secara default, penggunaan cookie bisa menjadi berbahaya. Hal ini terjadi jika kita menyimpan informasi 'penting' di dalam cookie tersebut. Cookie yang dikirim, secara default, tidak terenkripsi sehingga siapapun sebenarnya dapat melihat apa isi di dalamnya. Risikonya adalah bisa terjadi pembajakan sesi (pencuri menamngkap cookie pengguna lal umenyamar sebagai penggna), serangan skrip lintas situs atau XSS (penyuntikkan kode berbahaya oleh browser pengguna), serangan CSRF (penyerang mengelabui pengguna agar secara tidak sadar melakukan suatu tindakan tanpa persetujuan mereka), dll. Untuk mengantisipasi serangan-serangan ini, django memiliki CSRF token untuk memastikan bahwa setiap form yang akan dikirim pengguna (req POST) memang benar" dari pengguna aslinya. Selain itu, django juga hanya menyimpan session id di cookie dan data penting lainnya berada di server. Hal ini membuat data menjadi lebih aman.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Untuk melakukan hal ini, pertama saya mengimpor function bawaan django berupa UserCreationForm, messages, AuthenticationForm, authenticate, login, logout. Setelah itu, saya membuat function masing"nya. 
-Pada function register, saya membuat form baru yang kosong lalu di render menggunakan register.html agar client dapat melihat halaman field registrasi. Template register.html yang digunakan pun menggunakan bawaan django yang hanya menggunakan `{{ form.as_table }}`. Setelah client mengisi field kosong yang ada lalu menekan register, request methodnya berubah menjadi 'POST' lalu UserCreationFOrm yang baru akan dibuat berdasarkan QueryDict dari client. Setelah form nya valid, semua yang wajib diisi terisi, server akan membuat dan menyimpan data dari form tersebut. Setelah itu akan ada pesan pemberiahuan kalau proses pendaftaran akun berhasil. 
-Pada function login, pertama akan di cek apakah request dari client adalah 'POST' (sudah menekan login). Jika belum, maka server akan membuat authentication form yang baru agar client bisa beliha form login kosong lalu mengisinya. Sama seperti register, form ini dirender menggunakan template login.html yang dibuat dengan bawaan django. Setelah user menekan login (request method menjadi 'POST'), maka akan dibuat form baru berdasarkan QueryDict yang dikimkan oleh client. Jika data yang terisi sudah valid, maka akan diambil user yang sesuai. Setelah itu, akan dibuat session di server tsb dan user id akan tersimpan ke session nya. Setelah itu akan pergi ke halaman show_main.
-Pada function logout, pertama function akan menghapus sesi engguna yang saat ini masuk lalu mengarahkan ke halaman login.
2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
LINK : https://drive.google.com/drive/folders/1z2IoeBTCLMJiH4H_1jMbflszsmPKkxkw?usp=sharing
3. Menghubungkan model Product dengan User.
Hal pertama yang dilakukan adalah Product (di models.py) mengambil foreign key dari User sehingga tiap product yang dibuat akan tersambung pada user yang membuatnya. Untuk melakukan penyesuaian, ketika pembuatan product di create_product, tiap NewsForm yang berhasil dibuat akan di-set dulu usernya dengan user yang melakukan request baru disimpan ke database. Lalu dibuat juga filter pada show_main untuk melihat apakah user sudah terhubung dengan product yang dibuatnya. Di show_main jika filter typenya all maka akan mengambil seluruh product, jika tidak maka product akan difilter berdasarkan user pemiliknya. Karena dirender pada main.html, maka pada main.html dibuat button untuk memilih tipe pemfilteran yang ingin dipilih.
4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Untuk menampilkan informasi pengguna yang sedang login, misalnya nama user, kita cukup mengganti detail informasi pada template show_product.html nya. Kita bisa menampilkan nama user cukup dengan
`{% if product.user %}
    <p>Shopname: {{ product.user.username }}</p>
{% else %}
    <p>Shopname: Anonymous</p>
{% endif %}`
Hal ini dilakukan karena bisa saja ada product yang tidak tercatat user nya sehingga kita set anonymus. Jika ada, kita tampilkan nama usernya. Untuk menerapkan cookie berupa last_login, pertama kita bisa mengimpor dulu 
`import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse`
Setelah itu, pada saat login, kita set cookie nya pada tanggal dan jam saat ini.  Di show_main juga kita tambahkan key dan value dictionary yaitu `'last_login': request.COOKIES.get('last_login', 'Never')` dan saat logout kita hapus cookie nya dengan `response.delete_cookie('last_login')`. Setelah itu kita tampilkan last_login dengan menambah line `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada template main.html agar bisa dilihat oleh client.
</details>

<details>
<summary>Tugas Individu 5</summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat dua atau lebih aturan css yang diterapkan pada element yang sama, maka deklarasi css yang memiliki prioritas yang lebih tinggi yang akan dilayani/diterapkan. CSS dengan prioritas tertinggi adalah css yang ditulis inline pada elemen HTML. Selector ini akan meng-override semua aturan css pada selector lainnya.Selector ini ditandai dengan penggunaan `style=` sebagai atribut elemen tersebut. Prioritas kedua adalah Id Selector. Selector ini akan menimpa aturan css yg diterapkan oleh class selector, attribut selector, pseudo class, elemen dan pseudo-elements, dan universal selector. Penggunaannnya ditandai oleh `#<nama-id>` untuk menerapkan aturan pada id elemen tersebut. Prioritas selanjutnya adalah class selector, attribut selector, dan pseudo-classes. Selector ini akan menimpa aturan css dari element, pseudo-element, dan universal selector. Penggunaannya ditandai oleh `.<nama-class>`, `[<nama-attribute>=<value>]`, `:hover`, dan `:focus`. Prioritas selanjutnya adalah element dan pseudo-element. Selector ini akan meinmpa universal selector. Penggunaanya ditandai oleh `<nama-element> { <nama-attribute>: <value>; }` dan 
`<nama-elemen>::before { <nama-attribute>: <value>; }`. Prioritas terakhir adalah universal element. Selector ini akan ditimpa oleh selector lainnya jika ada 2 aturan css yanng diterapkan oleh suatu elemen. Penggunaan selector ini ditandai oleh `* { <nama-attribut>: <value>; <nama-attribut>: <value>; }`. 

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design menjadi konsep yang penting karena mendukung konsistensi tampilan web dan meningkatkan pengalaman pengguna melalui seluruh device. Web membuat pengguna lebih nyaman, mudah menavigasi dan cepat diakses. Selain itu, responsive design meningkatkan efisiensi karena memudahkan develooper untuk mengelola situs dan tidak perlu membuat dua versi berbeda web untuk mobile dan desktop. Reponsive design juga meningkatkan kemungkinan user untuk melakukan tindakan yang diinginkan oleh developer (Boosts conversion rates), misalnya oembelian. Selain itu, responsive deign dapat memastikan aksesibilitas dan mengurangi biaya pembuatan. 
-Contoh yang sudah menerapkan responsive design : youtube.com, tampilan menu di hp tidak terlihat, tetapi jika tombol burger dipencet, menu nya jadi terlihat.
-COntoh yang belum menerapkan responsive design : aren cs ui, tambilan di hp dan di laptop sama saja.
LINK : https://drive.google.com/drive/folders/1jz594u6uPnwvoTHAmoaP7rDeiHzeM9zO?usp=sharing

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Padding adalah komponen css yang memberikan ruang di dalam elemen untuk mencegah konten menempel langsung ke tepi elemennya dan menambah area dalam elemen. Komponen padding memungkinkan kita mengontrol seberapa dekat konten dengan batas luar elemen. Sedangkan margin adalah komponen css yang memberikan ruang di luar border elemen untuk membuat jarak antar elemen agar tidak terlalu rapat. Perbedaannya dengan padding adalah margin mengatur jarak di luar elemen, sedangkan padding di dalam elemen. Adapun, border  adalah komponen css berupa tampilan garis yang terlihat atau tidak terlihat yang mengelilingi sebuah elemen, border ini akan membungkus 'konten dari elemen' dan 'paddingnya'. Border berguna untuk meberikan batas pemisah antar elemen. 
-Pengimplementasian dari padding dapat dilakukan dengan mengatur atribut `padding, padding-top, padding-bottom, padding-left, padding-right` di dalam bagian selectornya.
-Pengimplementasian dari margin dapat dilakukan dengan meengatur atribut `margin, margin-top, margin-bottom, margin-left, margin-right` di dalam bagian selectornya.
-Pengimplementasian dari border dapat dilakukan dengan meengatur atribut `border, border-radius, border-style, border-color, border-width` di dalam bagian selectornya.
Masing-masinga atribut di atas diletakkan dalam sebuah selector dengan format:
`<nama-class/id/elemen>{
    <nama-atibut>: <value>;
}`
Value yang dapat diterapkan bisa berupa ukuran absolut berupa px, cm, mm, in, pt, pc ataupun ukuran relatif seperti %, em, rem, vh, dll.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
-Konsep Flex Box Layout adalah cara layouting satu dimensi yang berfokus pada elemen itu sendiri (item) sebagai unit terkecil dair susunan layoutnya. Elemennya disebut sebagai flex items dan secara keseluruhan disebut sebagai flex container. Konsep ini cocok digunakan untuk mengatur selemen dalam satu baris atau satu kolom saja. Contoh penggunaanya adalah ketika membuat menu navigasi secara horizontal/vertikal.
-Konsep Grid Layout adalah cara layouting dua dimensi yang direpresentasikan oleh baris dan kolom. Banyaknya kolom dan baris pada konsep grid perlu didefinisikan dahulu menggunakan `grid-template-columns` dan `grid-template-rows`. Elemen nya disebut sebagai grid items dan secara keseluruhan layoutingnya disebut grid container. Grid layout cocok diterapkan pada strukytur halaman yang kompleks dan membutuhkan penempatan elemen yang presisi pada suatu baris/kolom. Contoh penggunaannya adalah ketika membuat layout dari website yang membutuhkan bagian header, sidebar, maincontent, dan footer, atau penataan dalam produk e-commerce.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Implementasikan fungsi untuk menghapus dan mengedit product.
Pada template card tiap produk, buat button yang mengarah pada function edit_product dan delete_product di aplikasi main. Tentunya diberikan syarat bahwa akan ditampilkan jika user terdaftar dan produk tsb adalah milik usernya. Template juga akan mem-parsing id dari produj
-Pada edit_product, dicari produk dgn id tsb lalu ditampilkan dengan productForm. Jika perubahan sudah selesai dan requestnya menjadi POST, maka produk tersebut akan disimpan kembali ke database ulang lalu diarahkan ke halaman utama lagi. Jika belum POST, maka tampilan nya berupa form dari Productnya dengan merender edit_product.html.
-Pada delete_product, dicari produk dengan id yang diberikan. Lalu tinggal menggunakan `.delete` untuk menghapus setelah itu akan diarahkan kembali ke halaman utama.

2. Kustomisasi desain pada template HTML yang telah dibuat.
Perubahan sebenernya terjadi pada html html nya. Terutama di bagian card_product. Kali ini pembagian struktur halaman/html nya menggunakan class-class yang sudah disediakan oleh tailwind.
</details>

<details>
<summary>Tugas Individu 5</summary>

### Apa perbedaan antara synchronous request dan asynchronous request?
Perbedaannya terletak pada proses eksekusi yang dilakukan. Pada synchronus request, kode dieksekusi secara berurutan atau satu per satu. Program harus menyelesaikan tugas pertama sebelum mengerjakan tugas keduanya. Synchronus dapat membuat program terjebak dalam satu tugas dalam waktu yang lama, sebelum akhirnya melanjutkan tugas berikutnya. Hal ini membuat kinerja menjadi lambat dan kurang responsif. Sedangkan, dalam Asynchronus, pengeksekusian program dilakukan secara bersamaan. Program tidak perlu menunggu tugas pertama selesai untuk melakukan tugas kedua. Setiap tugas yang dijalankan, dieksekusi secara independen satu sama lain. Hal ini membuat efisiensi dan kecepatan lebih besar dalam pengeksekusian beberapa tugas sekaligus.

### Bagaimana AJAX bekerja di Django (alur request–response)?
PROSES AJAX BEKERJA:
Ketika suatu event terjadi di browser, javascript akan menangkangkap event tersebut. Setelah itu javascript akan membuat objek XMLHttpRequest dan mengirimkan nya ke server. Request ini akan diterima oleh url tertentu di django. Setelah itu, django menerima dan memproses request di views yang sesuai. Setelah itu, django server akan mengembaikan response dalam bentuk json, bukan seluruh page. Karena itu, tidak ada reload halaman yang terjadi, hanya pengiriman data dalam ukuran kecil. Di client, javascript menerima data json dari django server lalu mengubah tampilan dom sesuai data yang diterima. Akhirnya hanya sebagian kecil halaman saja yang berubah.

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Karena penggunaan AJAX memungkinkan untuk web page berkomunikasi tanpa me-reload seluruh halaman, hal ini membuat program lebih efisien, responsif, dan cepat. Pengeksekusian program dilakukan di sisi client, bukan dari server, menampilkan perubahan secara cepat pada halaman tanpa menunggu server. Beban pekerjaan server juga menjadi lebih ringan karena hanya mengambil informasi yang dibutuhkan. Selain itu, program bisa dijalankan secara event-driven. Program tidak perlu terus menerus me-refresh halaman, tetapi hanya bereaksi ketika pengguna menyebabkan suatu event. Program menjadi lebih interaktif tanpa harus me-reload halaman. 

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Cara memastikan keamanannya dengan memberikan perlindungan berupa CSRF token pada form login dan register. Setiap client me-load form login dan register, server membuatkan token csrf nya dan mengirimkannya pada client. Dengan begitu, setiap request yang dikirim oleh client akan diperiksa terlebih dahulu token scrf nya di cookie oleh server dan di cek apakah cocok atau tidak. Selain itu, django juga memiliki library tambahan berupa `django-ratelimit` untuk membatasi client mengirim request ke suatu endpoint. Perlindungan ini membuat akun client lebih aman karena mencegah adanya bruteforce yang dikirim oleh attacker. Jika request yang dikirim sudah terlalu banyak, django akan memberikan respon 429 (Too Many Request). Selain itu, library ini mencegah pembuatan banyak akun yg otomatis. Requet dalam waktu tertentu akan tercatat dan dihentikan apabila sudah mencapai batasnya.

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Dengan AJAX, website akan lebih menarik, interaktif, dan terasa lebih cepat digunakan karena tidak memperbarui keseluruhan halaman. Client tidak perlu pindah halaman untuk mengisi sebuah form. Selain itu, client akan merasa lebih puas karena ia tidak perlu selalu melakukan refresh untuk melihat data terbaru dari sebuah web. AJAX menjamin data terbaru ditampilkan oleh DOM. AJAX juga dapat membuat pengguna tetap berada di konteks yang sama tanpa reload. AJAX dapat menyimpan halaman secara otomatis tanpa mengganggu input yang sebelumnya telah dimasukkan. Pengguna tidak akan kehilangan data yang sedang diinput. Dengan AJAX, website menjadi efisien karena menghemat waktu loading yg disebabkan oleh memuat halaman baru. 

tes
tes
</details>