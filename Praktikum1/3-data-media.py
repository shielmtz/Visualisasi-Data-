#import library
import streamlit as st
from pathlib import Path
import base64
from PIL import Image

with st.container(border=True):     # untuk membuat bingkai/border
    st.title("Praktikum 1 Visualisasi Data") # untuk menampilkan judul utama
    st.subheader("Bagian 3 : Data Media") # untuk menampilkan judul tugas yang dikerjakan

    with st.container(border=True):     # untuk membuat bingkai/border
        st.markdown("""
        Kelompok 21:
        - IWANDA AULIA ROSANDO - 0110222095
        - RIO ADI SAPUTRO - 0110122076
        - SHILA MUMTAZ - 0110222039
        """)  # nama lengkap anggota - nim pakai markdown multibaris 
    st.write("Displaying an Images")
    # Displaying Image by specifying path
    st.image(r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\angsa.jpg")
    # Image Courtesy by pinterest

    st.write(
    "<p style='text-align:center; margin: 0.5rem 0;'>Image Courtesy: Pinterest</p>",
    unsafe_allow_html=True
    )
    # Image Courtesy
    st.write("Displaying Multiple Images")
    # Listing out animal images
    animal_images = [
        r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\angsa.jpg",
        r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\sapi.jpg",
        r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\ayam.jpg",
        r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\kambing.jpg",
        
    ]
    # Displaying Multiple Image with width 200
    st.image(animal_images, width=150 )

    # Image Courtesy
    st.markdown(
    "<p style='text-align:center; margin: 0.5rem 0;'>Image Courtesy: Pinterest</p>",
    unsafe_allow_html=True
    )

    # Function to set Image as Background
    def add_local_background_image_(image):
        with open(image, "rb") as image:
            encoded_string = base64.b64encode(image.read())
        st.write("Image Courtesy: pinterest")
        st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
        background-size:cover
        }}
        </style>
        """,
        unsafe_allow_html=True
            )
    st.write("Background Image")
    # Calling Image in function 
    add_local_background_image_( r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\angsa.jpg")
    original_image = Image.open(r"C:\xampp33\htdocs\PRAKTIKUM VISDAT\Praktikum1\asset\angsa.jpg")
    # Displaying Original Image
    st.title("Original Image")
    st.image(original_image)
    # Resizing Image to  600*400
    resized_image = original_image.resize((600, 400))
    # Displaying Resized Image
    st.title("Resized Image")
    st.image(resized_image)
        


