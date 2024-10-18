import cv2
import numpy as np

def process_header_image(input_image_path, mask_image_path, output_image_path):
    # 入力画像を読み込む
    input_image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    
    # マスク画像を読み込み、グレースケールに変換
    mask_image = cv2.imread(mask_image_path, cv2.IMREAD_GRAYSCALE)
    
    # マスク画像を入力画像と同じサイズにリサイズ
    mask_image = cv2.resize(mask_image, (input_image.shape[1], input_image.shape[0]))
    
    # 入力画像にアルファチャンネルがない場合は追加
    if input_image.shape[2] == 3:
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2BGRA)
    
    # マスクを適用
    input_image[:, :, 3] = mask_image
    
    # 結果を保存
    cv2.imwrite(output_image_path, input_image)

    return output_image_path
