<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0066CC,100:00BFA6&height=230&section=header&text=MyDocument%20&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=Document%20Management%20%7C%20Text%20Cleaning%20%7C%20Fullstack%20Python&descAlignY=60&descSize=18" />
</p>

<div align="center">

[![Fullstack](https://img.shields.io/badge/Architecture-Fullstack-brightgreen?style=for-the-badge)](#)
[![Backend](https://img.shields.io/badge/Backend-Python-blue?style=for-the-badge&logo=python)](https://python.org)
[![Frontend](https://img.shields.io/badge/Frontend-JS%20%7C%20HTML%20%7C%20CSS-orange?style=for-the-badge&logo=javascript)](https://developer.mozilla.org)

**Sistem pengelolaan dokumen terintegrasi yang memisahkan logika backend yang kuat dengan interface frontend yang responsif.**

</div>

---

## 🔄 Alur Kerja Aplikasi
<p align="center">
  <img src="image/alur.webp" alt="Alur MyDocument" width="85%" />
</p>

---

## 📑 Mengenai Proyek
**MyDocument App** dirancang dengan arsitektur *decoupled*. Backend menangani pemrosesan teks berat, pembersihan data (*text cleaning*), dan interaksi database, sementara Frontend fokus pada pengalaman pengguna yang intuitif.



---

## 📂 Struktur Proyek (Architecture)
Proyek ini terbagi menjadi dua folder utama untuk menjaga kode tetap bersih dan mudah dikembangkan:

```bash
mydocument/
├── ⚙️ backend/                # Core Logic & Data Processing
│   ├── generator.py          # Modul pemrosesan dokumen & text cleaning
│   ├── main.py               # Entry point API (Flask/FastAPI)
│   ├── models.py             # Definisi skema database & struktur data
│   └── 🗄️ database/           # Folder khusus penyimpanan SQLite
│
└── 🎨 frontend/               # User Interface & Interaction
    ├── index.html            # Struktur utama halaman (HTML5)
    ├── style.css             # Desain visual & layouting (CSS3)
    └── app.js                # Logic sisi klien & Fetch API (JS)
