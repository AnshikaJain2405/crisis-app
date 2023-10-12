import streamlit as st
from streamlit_chat import message
from streamlit_extras.switch_page_button import switch_page

message("Hi, please select your query") 
st.markdown('Select type of issue')
if (st.button('How does this app work?')):
    st.write('adhcubahcbj')

if(st.button('What to do in case of emergency')):
    st.write("blah blah")





if st.button('Back to Personal Information Page'):
    switch_page('Crisis_App')
