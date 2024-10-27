import cv2
import numpy as np
from PIL import Image
import io

def process_image(image, mask_image, alpha=0.5):
    """画像処理を行う関数"""
    # PILイメージをnumpy配列に変換
    if isinstance(image, Image.Image):
        image = np.array(image)
    if isinstance(mask_image, Image.Image):
        mask_image = np.array(mask_image)

    # 画像のチャンネル数を確認し、必要に応じて変換
    if len(image.shape) == 2:  # グレースケール
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGRA)
    elif image.shape[2] == 3:  # BGR
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    elif image.shape[2] == 4 and image.dtype == np.uint8:
        pass  # すでにBGRA形式
    
    if len(mask_image.shape) == 2:  # グレースケール
        mask_image = cv2.cvtColor(mask_image, cv2.COLOR_GRAY2BGRA)
    elif mask_image.shape[2] == 3:  # BGR
        mask_image = cv2.cvtColor(mask_image, cv2.COLOR_BGR2BGRA)
    elif mask_image.shape[2] == 4 and mask_image.dtype == np.uint8:
        pass  # すでにBGRA形式

    # マスク画像のリサイズ
    mask_image = cv2.resize(mask_image, (image.shape[1], image.shape[0]))

    # マスク画像のアルファチャンネルを取得
    mask_alpha = mask_image[:, :, 3]

    # 入力画像のアルファチャンネルを更新
    # マスクのアルファ値を使って元の画像のアルファ値を減算
    image[:, :, 3] = np.maximum(image[:, :, 3] - (mask_alpha * alpha).astype(np.uint8), 0)

    return image

def convert_to_pil(image):
    """numpy配列をPIL Imageに変換"""
    if isinstance(image, np.ndarray):
        return Image.fromarray(image)
    return image

def prepare_image(uploaded_file):
    """アップロードされたファイルを画像として準備"""
    if uploaded_file is None:
        return None
    
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes))
    
    # RGBAモードに変換
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    return image
