<div align="center">

<<img src="https://www.shutterstock.com/shutterstock/photos/2697012297/display_1500/stock-photo-vibrant-dark-blue-abstract-background-with-smooth-gradient-waves-and-soft-light-reflections-modern-2697012297.jpg" width="100%" alt="MyDocument App Banner" />

[![Fullstack](https://img.shields.io/badge/Architecture-Fullstack-brightgreen?style=for-the-badge)](#)
[![Backend](https://img.shields.io/badge/Backend-Python-blue?style=for-the-badge&logo=python)](https://python.org)
[![Frontend](https://img.shields.io/badge/Frontend-JS%20%7C%20HTML%20%7C%20CSS-orange?style=for-the-badge&logo=javascript)](https://developer.mozilla.org)

**Sistem pengelolaan dokumen terintegrasi yang memisahkan logika backend yang kuat dengan interface frontend yang responsif.**

---
</div>

## 📑 Mengenai Proyek
**MyDocument App** dirancang dengan arsitektur *decoupled*. Backend menangani pemrosesan teks berat, pembersihan data (*text cleaning*), dan interaksi database, sementara Frontend fokus pada pengalaman pengguna yang intuitif.



---

## 📂 Struktur Proyek (Architecture)
Proyek ini terbagi menjadi dua folder utama untuk menjaga kode tetap bersih dan mudah dikembangkan:

```bash
mydocument/
│
├── ⚙️ backend/               # Logic & Data Processing
│   ├── generator.py         # Modul pembuatan/pemrosesan dokumen
│   ├── main.py              # Entry point API (Flask/FastAPI)
│   ├── models.py            # Definisi skema database & struktur data
│   └── 🗄️ database/          # Penyimpanan database SQLite
│
└── 🎨 frontend/              # User Interface
    ├── index.html           # Struktur utama halaman
    ├── style.css            # Styling & Layouting
    └── app.js               # Logic interaksi di sisi client (Fetch API)