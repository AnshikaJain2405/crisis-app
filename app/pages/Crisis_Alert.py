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
from streamlit_extras.switch_page_button import switch_page

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(nrows=8)

# Print results.
for row in df.itertuples():
    if pd.notnull(row):
        st.write(f"{row.Facility}:  {row.Number}")

# df = conn.read(
#     worksheet="Sheet1",
#     ttl="10m",
#     usecols=[0, 1],
#     ,
# )

col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button('Help'):
        switch_page('Help')