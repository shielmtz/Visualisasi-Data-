# import library yang dibutuhkan
import streamlit as streamlit
import streamlit as st
# text element
# === Area Percobaan ===
with st.container(border=True): # untuk membuat bingkai/border
    st.markdown("### Percobaan Praktikum")
    st.caption("Gunakan area ini untuk uji coba sebelum versi final.") 
    # header =-untuk membuat tulisan header 
    st.header ("Display teks element") # untuk membuat header
    st.subheader("ini sub header ") # untuk membuat subjudul yang lebih kecil
    st.text("ini text") # untuk membuat teks polos tanpa format
    st.markdown ("**ini teks bold** dan *ini teks italic*") #markdown untuk memformat teks tebal/miring
    st.markdown("""
    - ini baris 1 
    - ini menggunakan markdown multibaris 
    """)
    st.caption("ini captionst.title")# teks kecil dibawah element (untuk penjelasan)
    st.title("ini judul")


# coba mandiri
# === Area Praktikum Asli ===
with st.container(border=True):     # untuk membuat bingkai/border
    # tuliskan:
    # 1. judul prktikum pakai title()  = Praktikum 1 visualisasi DAta
    st.title("Praktikum 1 Visualisasi Data")
    # 2. bagian ini pakai subheader() = bagian 1 : teks element
    st.subheader("Bagian 1 : Teks Element")
    # 3. nama lengkap anggota - nim pakai markdown multibaris """
    st.markdown("""
    Kelompok 21:
    - IWANDA AULIA ROSANDO - 0110222095
    - RIO ADI SAPUTRO - 0110122076
    - SHILA MUMTAZ - 0110222039
    """)
    # Bagian 2: menampilkan  rumus (LaTeX)
    st.header("Display Latex")  # untuk membuat judul materi bagian 2 menggunakan header
    st.latex (r''' \cos^2\theta = 1-2\sin^2\theta''') # rumus trigonometri
    st.latex (r''' (a+b^2 = a^2 +b^2 + 2ab )''') # rumus kuadrat binominal
    st.latex(r'''\frac{\partial u}{\partial t} =h^2 \left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} /\right)''') # persamaan difusi tiga dimensi


    # Bagian 3: Menampilkan kode Program
    st.header("Display Code")       # untuk membuat judul materi bagian 3 menggunakan header
    st.subheader("Python Code")     # untuk membuat subheader

    # simpan ke variabel 
    code = '''
    def hello():
        print ("Hello, Streamlit!")
    '''

    #st.code() untuk menampilkan potongan code dengan format rapi dan syntax highlighting
    st.code(code, language='python')
    st.subheader("""Java Code""")
    st.code("""public class GFG {
        public statis void  main (String args[]) {
        System.out.println("Hello World!);
        }
        }""", language= 'javascript')

    # fungsist.code() 2bisa digunakan untuk bahasa pemrograman lain  seperti java, javascript, c++, HTML, dll

    st.subheader("""Javascript Code""")
    st.code(""" <p id="demo"></p>
        <script>
        try{
        adddlert("Welcome guest!");
        // kesalahan ketik (adddlert) sengaja dibuat untuk menimbulkan error
        }
        catch(err) {
        document.getElementById("demo").innerHTML = err.message;
        // menampilkan pesan error di element HTML dengan id 'demo'}
        </script>
        """)







    
    

