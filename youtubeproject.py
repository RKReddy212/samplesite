import streamlit as st
st.title('FIRST WEB APPLICATION')
name = st.text_input("Enter your Name")
B = st.button('submit')
if B :
    st.write(f"HI {name}")