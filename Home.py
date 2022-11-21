import streamlit as st 
from brushing.canvas import show_canvas
import os 
from PIL import Image
import shutil
import subprocess

st.set_page_config(page_title='Remove Your Ex', 
                   page_icon=None, 
                   layout="centered", menu_items=None)




st.markdown("<h1 style='text-align: center; font-size: 5em; margin-bottom: -50px'>Remove Your Ex</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-style: italic'>Quick and easy tool to remove your ex from any picture 💔</h2>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.image('img/before.jpeg', caption='With the ugly stupid ex')
with col2:
    st.image('img/after.jpeg', caption='Without the ugly stupid ex')

def cleanup():
    for f in os.listdir('lama/input'):
        os.remove('lama/input/' + f)
    for f in os.listdir('lama/output'):
        os.remove('lama/output/' + f)
    uploaded_file = st.session_state['uploaded_file']
    Image.open(uploaded_file).save('lama/input/' + uploaded_file.name)
    ext = uploaded_file.name.split('.')[-1]
    if ext != 'png':
        shutil.copyfile('lama/input/' + uploaded_file.name, 'lama/input/' + uploaded_file.name.replace(ext, 'png'))
        os.remove('lama/input/' + uploaded_file.name)

    

uploaded_file = st.file_uploader(label="Upload image of your ex", on_change=cleanup, key='uploaded_file')

if uploaded_file:
    

    mask_exist = show_canvas(uploaded_file)
    if mask_exist:
        st.write('running')
        # subprocess.run(['bash', 'execute.sh'])
    for f in os.listdir('lama/output'):
        st.image('lama/output/' + f )



        

st.markdown('---')



st.write('All rights reserved - Send dollars and nudes to edmond@smallpepe.com')