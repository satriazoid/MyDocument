<div align="center">

<img src="https://capsule-render.vercel.app/render?type=soft&color=auto&height=200&section=header&text=MyDocument%20App&fontSize=70&animation=fadeIn&fontAlignY=50" width="100%" />

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

**Solusi manajemen dokumen modern yang terstruktur, efisien, dan aman.**
*Didesain untuk menangani teks dan file dengan pendekatan minimalis.*

---
</div>

## 🌌 Tentang MyDocument
Banyak aplikasi manajemen dokumen yang terlalu berat. **MyDocument** hadir dengan pendekatan berbeda: **Ringan, Cepat, dan Fokus pada Data**. Aplikasi ini bukan sekadar tempat penyimpanan, tapi juga asisten pemrosesan teks yang memastikan setiap data yang masuk sudah dalam kondisi bersih dan siap pakai.

### 🛠️ Core Capabilities
* **Structured Storage**: Database SQLite yang solid untuk menjamin integritas data.
* **Automated Text Cleaning**: Modul cerdas untuk normalisasi teks secara *real-time*.
* **Centralized Repository**: Akses semua dokumen hanya dari satu pintu API.
* **Developer Friendly**: Arsitektur modular yang memudahkan kustomisasi lebih lanjut.

---

## 🏗️ Arsitektur Proyek
Struktur folder dirancang mengikuti standar industri untuk pemisahan *concern* (Separation of Concerns):

```bash
mydocument/
├── 📄 app.py              # Entry point aplikasi (Main Server)
├── 📦 requirements.txt    # Daftar dependency sistem
├── 📖 README.md           # Blueprint dokumentasi
│
├── 🗄️ database/
│   └── mydocument.db      # SQLite Database (Storage layer)
│
├── 🛣️ routes/
│   ├── text.py            # API logic untuk data berbasis teks
│   └── file.py            # API logic untuk manajemen file fisik
│
├── ⚙️ utils/
│   └── text_cleaner.py    # Engine pembersih & normalisasi teks
│
└── 📤 uploads/
    └── files/             # Vault penyimpanan file asli