import streamlit as st
from PIL import Image
import numpy as np
from modules.image_processor import process_image, prepare_image, convert_to_pil
from modules.mask_manager import MaskManager
from modules.utils import create_download_button

def main():
    # ワイドモードの設定
    st.set_page_config(layout="wide")

    st.markdown("""
    <div align="center">
    
    # Pic-to-Header

    <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/pic-to-header/refs/heads/main/assets/result.png" width="50%">

    [![GitHub license](https://img.shields.io/github/license/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/blob/main/LICENSE)
    [![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/stargazers)
    [![GitHub issues](https://img.shields.io/github/issues/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/issues)

    ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
    ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
    </div>
    """, unsafe_allow_html=True)

    st.write("Pic-to-Headerは、マスク画像と入力画像を使用してヘッダー画像を生成するPythonアプリケーションです。")
    st.write("マスク画像と入力画像をアップロードして、ヘッダー画像を生成します。")

    # 2段組レイアウトの作成（左側を狭く、右側を広く）
    control_column, display_column = st.columns([1, 2])

    with control_column:
        # マスク管理インスタンスの作成
        mask_manager = MaskManager()

        # マスク画像の取得方法を選択
        mask_source = st.radio(
            "マスク画像の取得方法を選択",
            ["プリセットから選択", "URLから取得", "ファイルをアップロード"]
        )

        mask_image = None
        if mask_source == "プリセットから選択":
            preset_name = st.selectbox(
                "プリセットを選択",
                mask_manager.get_preset_names()
            )
            mask_image = mask_manager.get_preset_mask(preset_name)
        
        elif mask_source == "URLから取得":
            mask_url = st.text_input("マスク画像のURLを入力")
            if mask_url:
                mask_image = mask_manager.load_mask_from_url(mask_url)
        
        else:  # ファイルをアップロード
            mask_file = st.file_uploader("マスク画像をアップロード", type=["png", "jpg", "jpeg"])
            if mask_file is not None:
                mask_image = Image.open(mask_file)

        # 透明度の調整
        alpha = st.slider("マスクの透明度", 0.0, 1.0, 1.0)

        # ファイルアップロード（複数ファイル対応）
        uploaded_files = st.file_uploader(
            "画像をアップロードしてください",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True
        )
        if mask_image:
            # マスク画像のプレビュー表示
            st.write("選択中のマスク画像:")
            st.image(mask_image, caption="マスク画像", use_column_width=True)
            
    with display_column:

        if uploaded_files:
            st.write("処理結果:")
            # 各画像の処理と表示
            for idx, uploaded_file in enumerate(uploaded_files):
                # 水平に2列で表示するための設定
                img_col1, img_col2 = st.columns(2)
                
                # 元画像の表示
                with img_col1:
                    st.write(f"元画像 {idx + 1}:")
                    st.image(uploaded_file, use_column_width=True)

                # 処理後の画像の表示
                with img_col2:
                    st.write(f"処理後 {idx + 1}:")
                    input_image = prepare_image(uploaded_file)
                    if input_image is not None:
                        result = process_image(input_image, np.array(mask_image), alpha)
                        result_pil = convert_to_pil(result)
                        st.image(result_pil, use_column_width=True)
                        
                        # ダウンロードボタンの作成
                        create_download_button(
                            result_pil,
                            f"header_{uploaded_file.name}"
                        )
                
                # 区切り線を追加（最後の画像以外）
                if idx < len(uploaded_files) - 1:
                    st.markdown("---")
                        
if __name__ == "__main__":
    main()
