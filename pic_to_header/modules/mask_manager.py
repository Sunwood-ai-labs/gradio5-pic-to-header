import requests
from PIL import Image
import io
from functools import lru_cache

class MaskManager:
    def __init__(self):
        self.default_mask_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/pic-to-header/refs/heads/main/assets/mask.png"
        self.presets = {
            "デフォルトマスク": self.default_mask_url,
        }

    @staticmethod
    @lru_cache(maxsize=32)
    def load_mask_from_url(url):
        """URLから画像を読み込む。失敗時はNoneを返す"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            image = Image.open(io.BytesIO(response.content))
            return image
        except Exception:
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
