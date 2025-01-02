import streamlit as st
from streamlit_option_menu import option_menu
st.title("Hi Buddy")
with st.sidebar:
    select = option_menu(
       menu_title ='project title',
       options=['Abstraction','Task','System requirements','Modules'],
    )