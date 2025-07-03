import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# --- KONFIGURASI TAMPILAN WEBSITE ---
st.set_page_config(
    page_title="Deteksi Telur Retak",
    page_icon="🥚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- JUDUL APLIKASI ---
st.title("🥚 Website Deteksi Telur Retak")
st.write("Unggah gambar telur untuk dideteksi kondisinya (Bagus atau Retak) menggunakan model YOLOv8.")

# --- FUNGSI UNTUK MEMUAT MODEL ---
# Menggunakan cache agar model tidak di-load berulang kali setiap ada interaksi
@st.cache_resource
def load_model(model_path):
    """Memuat model YOLOv8 dari path yang diberikan."""
    model = YOLO(model_path)
    return model

# --- MEMUAT MODEL ---
# Pastikan file 'best.pt' ada di folder yang sama
model = load_model('best.pt')

# --- WIDGET UNGGAH GAMBAR ---
uploaded_file = st.file_uploader(
    "Pilih gambar telur...",
    type=["jpg", "jpeg", "png"]
)

# --- PROSES DAN TAMPILKAN HASIL ---
if uploaded_file is not None:
    # Membaca file gambar yang diunggah
    bytes_data = uploaded_file.getvalue()
    image = Image.open(uploaded_file)

    st.write("")
    st.write("**Hasil Deteksi:**")

    # Membuat dua kolom untuk menampilkan gambar asli dan hasil deteksi
    col1, col2 = st.columns(2)

    # Tampilkan gambar asli di kolom pertama
    with col1:
        st.image(image, caption='Gambar Asli', use_column_width=True)

    # Lakukan deteksi dengan model YOLOv8
    results = model(image)

    # Ambil gambar hasil deteksi dengan kotak pembatas
    # .plot() akan menggambar kotak dan label pada gambar
    result_plot = results[0].plot(font_size=5) # Anda bisa ganti angka 5 sesuai kebutuhan

    # Konversi gambar hasil (yang dalam format BGR dari OpenCV) ke RGB untuk ditampilkan
    result_plot_rgb = cv2.cvtColor(result_plot, cv2.COLOR_BGR2RGB)

    # Tampilkan gambar hasil deteksi di kolom kedua
    with col2:
        st.image(result_plot_rgb, caption='Hasil Deteksi', use_column_width=True)

else:
    st.info("Silakan unggah sebuah gambar untuk memulai deteksi.")