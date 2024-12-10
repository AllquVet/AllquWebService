import streamlit as st


import streamlit as st


lista_horas=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00",)
option = st.selectbox(
    "How would you like to be contacted?",
    lista_horas,placeholder="Elija una hora disponible",index=None
)

st.write("You selected:", option)