#import library
import streamlit as st
import pandas as pd             # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np              # untuk membuat data namrik acak       
import altair as alt         # untuk membuat chart interaktif
import matplotlib.pyplot as plt

#menampilkan judul dan deskripsi
st.title("Praktikum 1 - Visualisasi Data")      #menampilkan judul utama di halaman
st.caption ("Bagian 2: Data Elements")          #menampilkan keterangan bagian 

#st.markdown digunakan untuk menampilkan teks dengan format markdown (bullet list, bold,italic, dll )
st.markdown("""
Kelompok 21:
- IWANDA AULIA ROSANDO - 0110222095
- RIO ADI SAPUTRO - 0110122076
- SHILA MUMTAZ - 0110222039
""")

# Dataframe  : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas 
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# menampilkan dataframe 
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

# highlight nilai terkecil disetiap kolom dataframe 
# axis=0 bekerja per kolom 
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
   np.random.randn(30,10),
   columns=('col_no %d' % i for i in range(10)) 
)

# menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
# Menampilkan metric tunggal (nilai utama + perubahan nilai)

# Metric Tunggal
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") # kenaikan 1.2 °C

# Metric sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default): naik -> hijau, turun -> merah
# - "inverse": kebalikannya (naik -> merah)
# - "off": tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# menampilkan indikator data 
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col2.metric(label="Pelanggan", value=100, delta=10, delta_color="off") # netral (tidak baik dan tidak buruk)

# Menampilkan metric tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # nkosong # naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") # penurunan

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10)) 
    )
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n',"\nWrite is Super function")
# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a','b']
)
# Defining Chart 
chart = alt.Chart(df).mark_bar().encode(
     x='a', y='b', tooltip=['a', 'b'])
# Defining chart in write() function
st.write(chart)


# Math calculation with no functions defined
"Adding 5 & 4 =", 5+4
# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
#DataFrame using Magic
df = pd.DataFrame({'col': [1,2]})
'dataframe', df
# Magic working on chart
fig, ax = plt.subplots()            # <- buat fig & ax dulu
ax.hist(np.random.logistic(10, 5, size=5), bins=15)
st.pyplot(fig)                      # lalu render ke Streamlit