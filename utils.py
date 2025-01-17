from PIL import Image
import numpy as np
import streamlit as st
import tempfile

@st.cache(show_spinner=True)
def process_image(uploaded_file):
    """Read uploaded file and convert it to PIL image"""
    tfile = tempfile.NamedTemporaryFile(delete=True)
    tfile.write(uploaded_file.read())

    image = Image.open(tfile)
    return image

def display_image(image):
    """Display uploaded image along with the buttons and choices"""
    category = ['Animal', 'Flower', 'Bird']
    image_column, category_column = st.columns(2)

    with image_column:
        st.image(image)
        predict_button = st.button('Predict!')
    with category_column:
        category_type = st.radio('Please select category: ', category)
        st.write('Image dimensions:')
        st.write(image.size)

    return category_type.lower(), predict_button

def display_sidebar(options):
    """Options, warnings and text to go to the sidebar."""
    st.sidebar.warning('Please enter a valid image with jpg, jpeg or png extension')
    st.sidebar.title('Explore the following: ')
    option = st.sidebar.selectbox('Please choose an option: ', options)
    st.sidebar.write('(Species encyclopedia coming soon!)')
    return option
