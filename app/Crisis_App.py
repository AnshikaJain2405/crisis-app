import streamlit as st
import datetime as dt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.title('Personal Information')

st.markdown("Please fill in the below information to proceed further. This information is collected for assistance in times of emergency. Only authorised persons will be allowed access to this information.")

name = st.text_input('Name')

maxDate = dt.date(1960, 1, 1)
minDate = dt.date(2020, 1, 1)
dob = st.date_input('Date of Birth', minDate, maxDate)

bloodgrp = st.selectbox('Blood group', ['A+', 'A-', 'B+', 'B-', "AB+", "AB-", "O+", "O-"])

Medical_History = st.text_input('Any Medical History of Concern')

states = pd.read_csv(r"C:\Users\anshi\Desktop\crisis app\data\states.csv")
state = st.multiselect('Select State', states)

if st.button('Next Page'):
    switch_page('Crisis_Alert')

if st.button('Help'):
    switch_page('Help')
    