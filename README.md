# Simulasi Analisis Sederhana Data Penjualan

Aplikasi ini menampilkan simulasi analisis penjualan berdasarkan kategori produk dan tahun, dengan fitur interaktif dan visualisasi yang menarik.

## 🔧 Fitur Aplikasi

| Fitur                        | Deskripsi                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| 🎛️ Sidebar Filter           | Pilih tahun dan kategori produk untuk memfilter data                     |
| 📅 Tabel Data                | Menampilkan data penjualan bulanan dari file CSV eksternal              |
| 📈 Grafik Interaktif        | Visualisasi tren penjualan menggunakan Altair chart                      |
| 🧮 Statistik Ringkas         | Checkbox dan Selectbox untuk menampilkan info rata-rata, total, dll      |
| 📝 Feedback User            | Input teks untuk masukan pengguna                                        |

## ✅ Komponen Streamlit yang Digunakan

- `st.title`
- `st.sidebar.slider`
- `st.sidebar.checkbox`
- `st.dataframe`
- `st.altair_chart`
- `st.checkbox`
- `st.selectbox`
- `st.text_input`
- `st.metric`
- `st.caption`
- `st.session_state`

## 🚀 Cara Menjalankan Aplikasi

1. Clone repository ini:
```bash
git clone https://github.com/mauliau/streamlit.git
cd streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
streamlit run simulasi_analisis_penjualan.py
```

## 🧾 Data
Data dibaca dari file: `data/penjualan.csv`

## 🌐 Link Deployment

➡️ [Simulasi Analisis Penjualan](https://app-apdujjko9ybvhexmfddgvy.streamlit.app/)

## 🧾 Lisensi

MIT License. Silakan gunakan dan modifikasi sesuai kebutuhan.
