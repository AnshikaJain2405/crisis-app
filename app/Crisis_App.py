import streamlit as st
import datetime as dt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import os

st.title('Personal Information')

st.markdown("Please fill in the below information to proceed further. This information is collected for assistance in times of emergency. Only authorised persons will be allowed access to this information.")

name = st.text_input('Name')

maxDate = dt.date(1960, 1, 1)
minDate = dt.date(2020, 1, 1)
dob = st.date_input('Date of Birth', minDate, maxDate)

bloodgrp = st.selectbox('Blood group', ['A+', 'A-', 'B+', 'B-', "AB+", "AB-", "O+", "O-"])

Medical_History = st.text_input('Any Medical History of Concern')

Emergency_contact = st.number_input('Contact information of Relatives to be contacted in case of accident', 0)

# from pathlib import Path

# states_csv = open(r'C:\Users\anshi\Desktop\crisis app\app\states.csv')
# # states_csv = Path(__file__).parents[1] / 'states.csv'
# # states_csv = pd.read_csv(r"")
# state = st.multiselect('Select State', states_csv)

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col4:
    if st.button('Next Page'):
        switch_page('Crisis_Alert')

with col3:
    if st.button('Help'):
        switch_page('Help')
