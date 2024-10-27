import streamlit as st
from PIL import Image
import io

def convert_image_to_bytes(image):
    """画像をバイト列に変換"""
    if image is None:
        return None
    
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def create_download_button(image, filename):
    """ダウンロードボタンを作成"""
    if image is not None:
        image_bytes = convert_image_to_bytes(image)
        st.download_button(
            label="画像をダウンロード",
            data=image_bytes,
            file_name=filename,
            mime="image/png"
        )
