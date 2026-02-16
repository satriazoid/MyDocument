# ──────────────────────────────────────────────────────────────────────
#   📄 MY DOCUMENT APP - Simple, Clean, & Organized
#   Manage, process, and store your documents without the mess.
# ──────────────────────────────────────────────────────────────────────

## 📌 Apa itu MyDocument?
Jujur saja, kita semua benci dokumen yang berantakan. **MyDocument** dibuat untuk jadi solusi simpel buat siapa saja (mahasiswa, researcher, atau dev) yang butuh tempat terpusat buat simpan teks dan file. 

Nggak cuma simpan, aplikasi ini punya "tukang bersih-bersih" otomatis (Text Cleaner) yang bakal ngerapiin simbol aneh atau spasi double di teks kamu sebelum masuk ke database.

---

## 🔥 Fitur Unggulan
- **Centralized Management**: Semua dokumen ngumpul di satu tempat, nggak perlu nyari-nyari folder lagi.
- **Smart Text Cleaning**: Normalisasi teks otomatis (hapus noise & simbol nggak penting).
- **Fast Search**: Cari dokumen yang kamu butuhin dalam sekejap.
- **SQLite Database**: Ringan, nggak perlu install server DB yang berat-berat.
- **RESTful API**: Gampang diintegrasikan ke front-end atau aplikasi lain.

---

## 🛠️ "Jeroan" Aplikasi
Kita pakai stack yang simpel tapi powerfull:
* **Language:** Python (The GOAT for text processing)
* **Framework:** Flask (Biar enteng & fleksibel)
* **Database:** SQLite (No-nonsense storage)
* **API Format:** JSON
* **Workspace:** VS Code

---

## 📂 Struktur Folder (Biar Nggak Bingung)
```text
mydocument/
├── app.py                # Jantungnya aplikasi
├── requirements.txt      # List belanjaan library
├── README.md             # Yang lagi kamu baca sekarang
│
├── database/
│   └── mydocument.db     # Tempat semua data bernaung
│
├── routes/
│   ├── text.py           # Logic buat inputan teks mentah
│   └── file.py           # Logic buat urusan upload file
│
├── utils/
│   └── text_cleaner.py   # Modul rahasia pembersih teks
│
└── uploads/
    └── files/            # Rumah buat file-file yang kamu upload