import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Title
st.title("📊 Analisis Sederhana Data Penjualan")

# Sidebar inputs
st.sidebar.header("Pengaturan")
tahun = st.sidebar.slider("Pilih Tahun", 2020, 2025, 2023)

# Checkbox multiselect untuk kategori
st.sidebar.markdown("**Pilih Kategori Produk:**")
kategori_list = ["Elektronik", "Pakaian", "Makanan", "Minuman", "Lainnya"]
kategori = [k for k in kategori_list if st.sidebar.checkbox(k, value=k in ["Elektronik", "Pakaian"])]

# Tombol generate data dan session state
if "data" not in st.session_state:
    st.session_state.data = None

if st.button("🔄 Generate Data Penjualan"):
    st.session_state.data = pd.DataFrame({
        "Tanggal": pd.date_range(start=f"{tahun}-01-01", end=f"{tahun}-12-31", freq='M'),
        "Penjualan": np.random.randint(1000, 5000, 12),
        "Kategori": np.random.choice(kategori_list, 12)
    })

if st.session_state.data is not None:
    data = st.session_state.data

    # Filter berdasarkan kategori
    filtered_data = data[data["Kategori"].isin(kategori)]

    # Show dataframe
    st.subheader("📅 Data Penjualan")
    st.dataframe(filtered_data)

    # Visualisasi interaktif dengan Altair
    st.subheader("📈 Grafik Penjualan Bulanan")
    chart = alt.Chart(filtered_data).mark_line(point=True).encode(
        x="Tanggal",
        y="Penjualan",
        color="Kategori"
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    # Checkbox dan selectbox
    st.subheader("🧮 Statistik Ringkas")
    if st.checkbox("Tampilkan Rata-rata Penjualan"):
        avg = filtered_data["Penjualan"].mean()
        st.metric("Rata-rata Penjualan", f"{avg:.2f}")

    opsi_statistik = st.selectbox("Pilih Statistik Tambahan", ["Maksimum", "Minimum", "Total"])
    if opsi_statistik == "Maksimum":
        st.info(f"📌 Penjualan Tertinggi: {filtered_data['Penjualan'].max()}")
    elif opsi_statistik == "Minimum":
        st.info(f"📉 Penjualan Terendah: {filtered_data['Penjualan'].min()}")
    else:
        st.info(f"🧾 Total Penjualan: {filtered_data['Penjualan'].sum()}")

    # Text input
    st.subheader("📝 Feedback")
    feedback = st.text_input("Masukkan saran untuk analisis ini:")
    if feedback:
        st.success("Terima kasih atas masukannya!")
else:
    st.warning("Klik tombol '🔄 Generate Data Penjualan' terlebih dahulu untuk memulai.")

