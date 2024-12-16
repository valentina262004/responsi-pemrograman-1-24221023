import streamlit as st

st.title("Hitung keliling dan luas")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
panjang = st.number_input("Masukan panjang persegi", value=0)
st.write("The current number is ", panjang)

lebar = st.number_input("Masukan lebar persegi", value=0)
st.write("The current number is ", lebar)

if (panjang & lebar):
    st.subheader('Keliling')
    st.write(2 * (panjang + lebar))
    st.subheader('Luas')
    st.write( panjang * lebar)