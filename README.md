# Source-Code-Comments-Cosine-Similarity-Checker

Website ini dirancang untuk menghitung skor kesamaan (similarity score) antara komentar kode buatan manusia dan komentar kode yang dihasilkan oleh model AI (seperti LLM – Large Language Models). Perhitungan similarity dilakukan dengan pendekatan **Sentence-BERT (SBERT)** untuk mendapatkan representasi vektor dari komentar, lalu dihitung tingkat kesamaannya menggunakan **cosine similarity**.

## 🎯 Tujuan
Membantu peneliti atau pengembang mengevaluasi kualitas komentar kode otomatis (AI-generated) dengan membandingkannya secara semantik terhadap komentar asli dari manusia.

## 🧠 Teknologi yang Digunakan
- **Frontend:** HTML, Bootstrap 5
- **Backend:** Python (Flask)
- **Model NLP:** Sentence-BERT (`sentence-transformers`)
- **Similarity Measure:** Cosine Similarity (`sklearn.metrics.pairwise.cosine_similarity`)

## ⚙️ Fitur Utama
- Input komentar kode dari manusia dan AI
- Hitung dan tampilkan nilai cosine similarity
- Visualisasi hasil perbandingan (piechart)

## 📌 Contoh Penggunaan
1. Masukkan komentar kode versi manusia dan versi AI.
2. Sistem menghitung representasi vektor dari kedua komentar menggunakan Sentence-BERT.
3. Cosine similarity dihitung dan ditampilkan sebagai nilai skor kesamaan.

## 📁 Struktur Proyek (Singkat)
- /templates # HTML templates (Flask)
- /static # Asset statis (CSS/JS)
- /app.py # Aplikasi utama Flask
- /similarity.py # Fungsi penghitungan Sentence-BERT + cosine similarity
- /README.md

## 🧪 Cocok Untuk
- Penelitian tentang dokumentasi otomatis menggunakan AI
- Analisis semantik komentar kode
- Evaluasi performa LLM dalam memahami dan menjelaskan kode

---
