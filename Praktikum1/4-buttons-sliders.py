import streamlit as st
import time


with st.container(border=True):     # untuk membuat bingkai/border
    # menampilkan judul dan deskripsi
    st.title("Praktikum 1 - Visualisasi Data")      #menampilkan judul utama di halaman
    st.caption ("Bagian 2: Data Elements")          #menampilkan keterangan bagian 

    # st.markdown digunakan untuk menampilkan teks dengan format markdown (bullet list, bold,italic, dll )
    st.markdown("""
    Kelompok 21:
    - IWANDA AULIA ROSANDO - 0110222095
    - RIO ADI SAPUTRO - 0110122076
    - SHILA MUMTAZ - 0110222039
    """)

    st.title('Creating a Button')
    # Defining a Button
    button = st.button('Click Here')
    if button:
        st.write('You Have clicked the Button')
    else:
        st.write('You have not clicked the button')

    st.title('Creating Radio Buttons')
    # Defining Radio Button 
    gender = st.radio("Select your Gender",('Male','Female', 'Others'))
    if gender == 'Male':
        st.write('You Have Selected Male.')

    elif gender == 'Female':
        st.write('You Have Selected Female.')

    else:
        st.write('You Have Selected Others.')

    st.title('Creating Checkboxes')
    st.write('Select your Hobies')
    # Defining Checkboxes
    check_1 = st.checkbox('Books')
    check_2 = st.checkbox('Movie')
    check_3 = st.checkbox('Sports')

    st.title('Creating Dropdown')
    # Defining Dropdown
    hobby = st.selectbox('Choose your hobby: ', ('Books', 'Movie', 'Sports'))

    st.title('Multi-Select')
    # Defining Multi-Select with Pre-Selection
    hobbies = st.multiselect('What are your Hobbies', 
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing'])

    st.title("Download Button")
    # Creating Download Button
    down_btn = st.download_button(
        label="Downloade Image",
        data=open("C:/xampp33/htdocs/PRAKTIKUM VISDAT/Praktikum1/asset/kambing.jpg", "rb"),
        file_name="kambing.jpg",
        mime="image/jpg"
    )

    st.title('Progress Bar')
    # Defining Progress Bar
    download = st.progress(0)
    for percentage in range(100):
        time.sleep(0.1)
        download.progress(percentage + 1)
    st.write('Download Complete')
    st.title('Spinner')
    # Defining Spinner
    with st.spinner('Loading...'):
        time.sleep(5)
    st.write('Hello Data Scientists')








