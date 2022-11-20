import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

def show_canvas(bg_image):
    # Specify canvas parameters in application
    drawing_mode = 'freedraw'

    stroke_width = st.slider("Brush stroke width: ", 10, 50, 25)
    stroke_color = 'white'

    realtime_update = st.checkbox("Update in realtime", True)
        
    background_image = Image.open(bg_image)
    og_height = background_image.height
    og_width = background_image.width
    height = og_height
    width = og_width
    if background_image.width > 1000:
        width = 1000 
        height = 1000 * background_image.height / background_image.width
    if background_image.height > 700:
        height = 700 
        width = 700 * background_image.width / background_image.height
    
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#eee",
        background_image=background_image,
        update_streamlit=realtime_update,
        height=height,
        width=width,
        drawing_mode=drawing_mode,
        point_display_radius= 0,
        key="canvas",
    )
    
    # Do something interesting with the image data and paths
    if canvas_result.image_data is not None:
        mask = Image.fromarray(canvas_result.image_data)
        mask = mask.resize([int(og_width), int(og_height)])
        ext = bg_image.name.split('.')[-1]
        mask.save('lama/input/' + bg_image.name.replace('.', '_mask.').replace(ext, 'png'))
        return True