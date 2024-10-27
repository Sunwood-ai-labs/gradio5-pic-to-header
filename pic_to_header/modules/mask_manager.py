import requests
from PIL import Image
import io
import streamlit as st

class MaskManager:
    def __init__(self):
        self.default_mask_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/pic-to-header/refs/heads/main/assets/mask.png"
        self.presets = {
            "デフォルトマスク": self.default_mask_url,
        }

    @staticmethod
    @st.cache_data
    def load_mask_from_url(url):
        """URLから画像を読み込む"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(io.BytesIO(response.content))
            return image
        except Exception as e:
            st.error(f"マスク画像の読み込みに失敗しました: {str(e)}")
            return None

    def get_preset_names(self):
        """プリセット名の一覧を取得"""
        return list(self.presets.keys())

    def get_preset_mask(self, preset_name):
        """プリセット名に対応するマスク画像を取得"""
        if preset_name in self.presets:
            return self.load_mask_from_url(self.presets[preset_name])
        return None

    def add_preset(self, name, url):
        """新しいプリセットを追加"""
        self.presets[name] = url
