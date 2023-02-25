import streamlit as st


st.title("Hospital Appointment Booking App")

with st.form(key='my_form'):
    username = st.text_input('ID')
    password = st.text_input('Password')
    st.form_submit_button('Login')
st.write(f'Not a member yet? Register')
    
st.header('Register')    
st.text_input('First name')
st.text_input('Surname')
st.text_input('Middle name')

st.text_input('Email')
st.number_input('Phone Number')

st.date_input('Your birthday')
st.slider("Age", 0,150)


st.radio("What is your gender", ["Male", "Female"]) 

st.text_input("Address")

st.button("submit")

st.header('Appointment Booking')

st.selectbox("Category", ["General Physician", "Bone", "Heart", "Dentist", "Eye", "Neurologist", "Kidney", "Cardiologist", "Plastic surgeon"])

st.selectbox("Doctor", ["ABC", "Lora Adeoye"])
                                                
st.date_input('Appointment Date')
st.time_input('Appointment Time') 

st.button("Check", "9.00-9.30, 9.30-10.00, 10.00-10.30")

st.button("Book")
