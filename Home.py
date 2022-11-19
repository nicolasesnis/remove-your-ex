import streamlit as st 

st.title('Remove Your Ex')
st.subheader("Quick and easy tool to remove your ex from any picture 💔")

col1, col2 = st.columns(2)
with col1:
    st.image('img/before.jpeg', caption='With the ugly stupid ex')
with col2:
    st.image('img/after.jpeg', caption='Without the ugly stupid ex')

uploaded_file = st.file_uploader(label="Upload image of your ex")
st.markdown('---')

st.write('All rights reserved - Send dollars and nudes to edmond@smallpepe.com')