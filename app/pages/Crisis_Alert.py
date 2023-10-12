# import streamlit as st

# if(st.button('I am in a minor Accident')):
#     st.link_button('Call Police')
#     st.link_button('Call Relative')
#     st.link_button()
   

# if(st.button(''))

# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples(index=True):
    if pd.notnull(row):
        st.write(f"{row.Facility}:  {row.Number}")