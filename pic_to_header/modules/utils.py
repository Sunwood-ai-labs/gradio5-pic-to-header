from PIL import Image
import io

def convert_image_to_bytes(image):
    """画像をバイト列に変換"""
    if image is None:
        return None
    
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def create_download_button(*args, **kwargs):
    """Streamlit専用の関数はGradio版では未使用。互換のため残置。"""
    raise NotImplementedError("create_download_button is not supported in Gradio UI")
