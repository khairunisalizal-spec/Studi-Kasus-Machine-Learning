# Studi Kasus Machine Learning: Prediksi Risiko Kelulusan Mahasiswa

Proyek pembelajaran untuk materi **Introduction to Machine Learning**. Aplikasi memperkirakan apakah seorang mahasiswa berpotensi lulus tepat waktu berdasarkan kehadiran, nilai tugas, dan nilai UTS.

> **Catatan penting:** data dalam proyek ini adalah data contoh/sintetis untuk latihan, bukan data mahasiswa nyata. Hasil prediksi bukan keputusan akademik dan tidak boleh dipakai untuk menilai mahasiswa tanpa verifikasi manusia.

## Teknologi
- Python
- Pandas
- Scikit-learn (StandardScaler + Logistic Regression)
- Flask
- HTML dan CSS

## Struktur proyek
```text
Studi_Kasus_Machine_Learning/
├── app.py
├── train_model.py
├── data_kelulusan.csv
├── requirements.txt
├── README.md
├── LAPORAN_STUDI_KASUS.md
├── .gitignore
└── templates/
    └── index.html
```

## Cara menjalankan di komputer
1. Pastikan Python 3.10 atau lebih baru sudah terpasang.
2. Ekstrak ZIP proyek ini, lalu buka foldernya di VS Code.
3. Buka Terminal pada folder proyek.
4. Buat virtual environment (opsional tetapi disarankan):
   ```bash
   python -m venv .venv
   ```
   Windows:
   ```bash
   .venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
5. Instal library:
   ```bash
   pip install -r requirements.txt
   ```
6. Latih dan evaluasi model:
   ```bash
   python train_model.py
   ```
7. Jalankan aplikasi web:
   ```bash
   python app.py
   ```
8. Buka alamat `http://127.0.0.1:5000` di browser.

Aplikasi juga akan membuat model otomatis saat pertama kali dijalankan jika file model belum tersedia.

## Cara mengunggah ke GitHub
1. Masuk ke https://github.com dan buat repository baru, misalnya `studi-kasus-machine-learning`.
2. Ekstrak ZIP dan buka terminal pada folder proyek.
3. Jalankan:
   ```bash
   git init
   git add .
   git commit -m "Tambah studi kasus machine learning"
   git branch -M main
   git remote add origin https://github.com/USERNAME/studi-kasus-machine-learning.git
   git push -u origin main
   ```
4. Ganti `USERNAME` dengan username GitHub sendiri. Jangan unggah data pribadi atau data mahasiswa sungguhan.

Jika Git belum terpasang, unggah isi folder melalui tombol **Add file → Upload files** di halaman repository GitHub.

## Alur Machine Learning
Pengumpulan data → pemeriksaan data → pembagian data latih dan uji → standardisasi fitur → pelatihan Logistic Regression → evaluasi akurasi, presisi, dan recall → simpan model → gunakan model melalui formulir web.

## Batasan
- Dataset kecil dan sintetis, sehingga metrik evaluasi tidak menunjukkan performa di dunia nyata.
- Prediksi hanya untuk demonstrasi konsep supervised learning.
- Sebelum penggunaan nyata, dibutuhkan data yang representatif, evaluasi lebih ketat, pemeriksaan bias, perlindungan privasi, dan pengawasan manusia.
