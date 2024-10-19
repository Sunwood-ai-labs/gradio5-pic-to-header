import streamlit as st
import os

# ページ設定
st.set_page_config(
    page_title="Pic-to-Header",
    page_icon="🖼️",
    layout="wide"
)

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    st.markdown(readme_content, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("README.mdが見つかりませんでした。")
