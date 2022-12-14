import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64 

   
st.set_page_config(layout="wide", page_title="Ramond Background Remover",page_icon="MY LOGO.png")

menu = ["Remove","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Remove":
    st.write("## Remove your image background")
    st.write(
        ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar."
        )
    st.write("## Upload and download")
    
    def convert_image(img):
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        return byte_im
    
    def fix_image(upload):
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)
        fixed = remove(image)
        col2.write("Background Image Removed :wrench:")
        col2.image(fixed)
        st.sidebar.markdown("\n")
        st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")

    col1, col2 = st.columns(2)
    my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if my_upload is not None:
        fix_image(upload=my_upload)
    else:
        fix_image("me.jpg")



if choice == "About":
    
    st.subheader("ABOUT THE DEVELOPER")
    st.text('''
       MY NAME IS FASASI ABDULRAHMAN TEMITOPE.
       I'M A MACHINE LEARNING AND ARTIFICIAL INTELLIGIENCE DEVELOPER.
       I CREATED THIS APPLICATION SO AS TO HELP PEOPLE TO BE ABLE TO REMOVE BACKGROUND FROM YOUR IMAGES.
       ''')
    image = Image.open("my.jpg")
    st.image(image,caption=None, width=490, use_column_width=100, clamp=False, channels="RGB", output_format="auto")

    
    st.subheader("ABOUT THE APP")
    st.text("BACKGROUND REMOVER")
    st.text("POWERED BY:FASASI ABDULRAHMAN TEMITOPE")
    st.text("I can see that you are impressed after checking my work")
    st.text("Oya start bringing work ooo")
    st.success("RAYTECH PROJECT")
    st.image("MY LOGO.png")
    st.balloons()            
    
