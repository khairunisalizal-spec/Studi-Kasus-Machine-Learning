# Laporan Studi Kasus Machine Learning
## Prediksi Risiko Kelulusan Mahasiswa

**Mata kuliah:** Introduction to Machine Learning  
**Pemateri:** Dr. Taniza Tajudin  
**Tanggal materi:** 16 Oktober 2026  
**Nama mahasiswa:** ................................  
**NIM:** ................................  
**Dosen pengampu:** ................................

## 1. Latar Belakang
Perguruan tinggi dapat memantau kehadiran dan hasil belajar untuk mengenali mahasiswa yang mungkin membutuhkan dukungan akademik lebih awal. Machine Learning (ML) dapat dipakai sebagai alat bantu untuk mempelajari pola dari data historis. Sistem pada studi kasus ini merupakan prototipe edukasi, bukan alat untuk menentukan kelulusan secara resmi.

## 2. Rumusan Masalah
Bagaimana membangun model sederhana yang memprediksi potensi kelulusan tepat waktu berdasarkan tiga indikator: persentase kehadiran, nilai tugas, dan nilai UTS?

## 3. Tujuan
1. Menerapkan konsep supervised learning.
2. Melatih model klasifikasi menggunakan Python.
3. Mengukur performa dengan akurasi, presisi, dan recall.
4. Menyediakan antarmuka HTML agar contoh prediksi mudah dicoba.

## 4. Data dan Fitur
Dataset contoh berisi 40 baris data sintetis. Fitur masukan adalah:
- `kehadiran`: persentase kehadiran, 0–100.
- `nilai_tugas`: nilai tugas, 0–100.
- `nilai_uts`: nilai UTS, 0–100.
- `lulus_tepat_waktu`: target kelas, 1 = berpotensi lulus tepat waktu dan 0 = perlu pendampingan.

Angka target dibuat untuk latihan dan tidak mewakili hubungan akademik yang tervalidasi.

## 5. Metode
Jenis pembelajaran yang digunakan adalah **Supervised Learning**, karena dataset memiliki label target. Algoritma yang digunakan adalah **Logistic Regression** untuk klasifikasi biner. `StandardScaler` membantu menyetarakan skala fitur.

Pembagian data dilakukan menjadi 75% data latih dan 25% data uji dengan `random_state=42` agar hasil pembagian dapat direproduksi. Metrik yang dicetak meliputi:
- **Akurasi:** proporsi seluruh prediksi yang benar.
- **Presisi:** proporsi prediksi kelas positif yang benar.
- **Recall:** proporsi data positif yang berhasil dikenali.

## 6. Implementasi
File `train_model.py` membaca data CSV, membagi data, melatih pipeline, mencetak evaluasi, dan menyimpan model. File `app.py` menjalankan aplikasi Flask dan memuat model. Halaman `templates/index.html` menyediakan formulir input dan menampilkan hasil prediksi.

Perintah:
```bash
pip install -r requirements.txt
python train_model.py
python app.py
```
Lalu buka `http://127.0.0.1:5000`.

## 7. Hasil dan Pembahasan
Saat `train_model.py` dijalankan, nilai akurasi, presisi, recall, dan laporan klasifikasi akan ditampilkan di terminal. Nilai tersebut perlu disalin ke laporan setelah menjalankan program. Karena dataset sangat kecil dan sintetis, skor bisa berubah jika data atau pembagian data berubah dan tidak boleh dianggap sebagai bukti bahwa model siap digunakan di kampus.

## 8. Etika dan Keterbatasan
- Data harus dikumpulkan secara sah dan dijaga kerahasiaannya.
- Model dapat mewarisi bias dari data historis.
- Prediksi yang keliru dapat memberi label yang tidak adil kepada mahasiswa.
- Mahasiswa perlu diberi kesempatan menjelaskan situasi yang tidak tercermin dalam angka.
- Hasil harus menjadi sinyal untuk menawarkan bantuan, bukan dasar tunggal untuk menghukum atau mengambil keputusan akademik.
- Pengawasan manusia dan evaluasi berkala tetap diperlukan.

## 9. Kesimpulan
Studi kasus ini menunjukkan alur dasar ML: menyiapkan data, melatih model, mengevaluasi hasil, lalu mengintegrasikannya ke aplikasi web. Model klasifikasi dapat membantu demonstrasi pengenalan pola, tetapi kualitas data, keadilan, privasi, dan penilaian manusia tetap penting.

## 10. Pengembangan Selanjutnya
1. Menggunakan dataset yang lebih besar dan tervalidasi dengan izin yang sesuai.
2. Menambahkan validasi silang dan confusion matrix.
3. Membandingkan Logistic Regression dengan Decision Tree.
4. Memeriksa fairness dan menjelaskan prediksi kepada pengguna.
5. Menyediakan dokumentasi dataset dan batasan model pada repository GitHub.
