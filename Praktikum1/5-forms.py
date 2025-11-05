import streamlit as st
import datetime
import pandas as pd

st.title("Text Box")
# Creating text box
name = st.text_input("Enter your Name")
st.write("Your Name is", name)

# Creating Text Area
input_text = st.text_area("Enter your Riview")
# Printing Entered Text
st.write("""You entered:\n""", input_text)
# Create Number Input
st.number_input("Enter Your Number")
# Create Number Input
num = st.number_input("Enter Your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n step Size value is 2")
st.write("Total value after adding Number entered with step value is;", num)

st.title("Time")
# Defining Time Function 
st.time_input("Select Your Time")
st.title("Date")
# Defining Time Function 
st.date_input("Select Your Date", value=datetime.date(1989, 12, 5),
min_value=datetime.date(1989, 1, 1),
max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
# Defining Color Picker 
color_code = st.color_picker("Select your Color")
st.header("color_code")

st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,"file_size":data_file_size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploader")

my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)
