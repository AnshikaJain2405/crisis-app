import streamlit as st
from streamlit_chat import message
from streamlit_extras.switch_page_button import switch_page

message("Hi, please select your query") 

st.markdown('Select type of issue')

if (st.button('How does this app work?')):
    st.write('adhcubahcbj')

if(st.button('What to do in case of emergency')):
    st.write("blah blah")

col1, col2, col3 = st.columns([1,1,1])

with col3: 
    if st.button('Prev Page'):
        switch_page('Crisis_App')
