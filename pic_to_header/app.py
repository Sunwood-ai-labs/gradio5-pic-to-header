import os
import tempfile
import zipfile
from typing import List, Optional, Any

import gradio as gr
from PIL import Image
import numpy as np

from .modules.image_processor import process_image, convert_to_pil
from .modules.mask_manager import MaskManager


mm = MaskManager()


# Custom theme using provided palette
# Palette:
#  - Light background: #FFFFFF
#  - Primary (accent): #4B2273
#  - Text (dark):      #07030D
#  - Secondary darks:  #160A26, #251240
def create_pictoheader_theme() -> gr.Theme:
    return (
        gr.Theme(
            primary_hue="slate",
            secondary_hue="stone",
            neutral_hue="zinc",
            text_size="md",
            spacing_size="lg",
            radius_size="lg",
            font=[
                "Hiragino Sans",
                "Noto Sans JP",
                "Yu Gothic",
                "system-ui",
                "sans-serif",
            ],
            font_mono=[
                "SF Mono",
                "Monaco",
                "monospace",
            ],
        ).set(
            body_background_fill="#FFFFFF",
            body_text_color="#07030D",

            button_primary_background_fill="#4B2273",
            button_primary_background_fill_hover="#251240",
            button_primary_text_color="#FFFFFF",

            button_secondary_background_fill="#160A26",
            button_secondary_background_fill_hover="#251240",
            button_secondary_text_color="#FFFFFF",

            input_background_fill="#FFFFFF",
            input_border_color="#251240",
            input_border_color_focus="#4B2273",

            block_background_fill="#FFFFFF",
            block_border_color="#251240",
            panel_background_fill="#FFFFFF",
            panel_border_color="#251240",

            slider_color="#4B2273",

            # ここがポイント：チェックボックスのラベル背景
            checkbox_label_background_fill="#4A2272",
            checkbox_label_background_fill_hover="#4A2272",
            checkbox_label_background_fill_selected="#4A2272",
            checkbox_label_background_fill_dark="#833CC9",
            checkbox_label_background_fill_hover_dark="#833CC9",
            checkbox_label_background_fill_selected_dark="#833CC9",

            # これがCSSの --checkbox-label-text-color
            checkbox_label_text_color="#FFFFFF",
            # 選択時の文字色（CSS: --checkbox-label-text-color-selected）
            checkbox_label_text_color_selected="#FFFFFF",
        )
    )
def _resolve_mask(mask_source: str,
                  preset_name: Optional[str],
                  mask_url: Optional[str],
                  mask_upload: Optional[Image.Image]) -> Optional[Image.Image]:
    if mask_source == "プリセットから選択" and preset_name:
        return mm.get_preset_mask(preset_name)
    if mask_source == "URLから取得" and mask_url:
        return mm.load_mask_from_url(mask_url)
    if mask_source == "ファイルをアップロード" and mask_upload is not None:
        return mask_upload
    return None


def update_mask_preview(mask_source, preset_name, mask_url, mask_upload):
    mask = _resolve_mask(mask_source, preset_name, mask_url, mask_upload)
    return mask


def _zip_images(images: List[Image.Image]) -> str:
    tmpdir = tempfile.mkdtemp(prefix="pic_to_header_")
    paths = []
    for i, img in enumerate(images):
        p = os.path.join(tmpdir, f"header_{i+1}.png")
        img.save(p, format="PNG")
        paths.append(p)
    zpath = os.path.join(tmpdir, "headers.zip")
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in paths:
            zf.write(p, arcname=os.path.basename(p))
    return zpath


def _load_pil_images_from_files(files: Optional[List[Any]]) -> List[Image.Image]:
    imgs: List[Image.Image] = []
    if not files:
        return imgs
    for f in files:
        path = None
        if isinstance(f, str):
            path = f
        elif isinstance(f, dict) and "path" in f:
            path = f.get("path")
        elif hasattr(f, "name"):
            path = getattr(f, "name")
        if path and os.path.exists(path):
            try:
                imgs.append(Image.open(path).convert("RGBA"))
            except Exception:
                pass
    return imgs


def generate(images: Optional[List[Any]],
             mask_source: str,
             preset_name: Optional[str],
             mask_url: Optional[str],
             mask_upload: Optional[Image.Image],
             alpha: float):
    pil_images = _load_pil_images_from_files(images)
    if not pil_images:
        return None, None, gr.update(value=None)

    mask = _resolve_mask(mask_source, preset_name, mask_url, mask_upload)
    if mask is None:
        return None, None, gr.update(value=None)

    results = []
    originals = []
    mask_np = np.array(mask)
    for img in pil_images:
        originals.append(img)
        out = process_image(img, mask_np, alpha)
        out_pil = convert_to_pil(out)
        results.append(out_pil)

    zip_path = _zip_images(results)
    return originals, results, zip_path


def build_demo():
    with gr.Blocks(title="Pic-to-Header (Gradio)") as demo:
        gr.Markdown(
            """
            <div align="center">
            
            # Gradio5 Pic-to-Header
            
            </div>
            """,
            elem_id="header_md"
        )

        with gr.Row():
            with gr.Column(scale=1):
                mask_source = gr.Radio(
                    ["プリセットから選択", "URLから取得", "ファイルをアップロード"],
                    label="マスク画像の取得方法",
                    value="プリセットから選択",
                )
                preset_name = gr.Dropdown(
                    choices=mm.get_preset_names(),
                    label="プリセット",
                    value=mm.get_preset_names()[0] if mm.get_preset_names() else None,
                )
                mask_url = gr.Textbox(label="マスク画像のURL")
                mask_upload = gr.Image(label="マスク画像をアップロード", type="pil")

                alpha = gr.Slider(0.0, 1.0, step=0.01, value=1.0, label="マスクの透明度")

                mask_preview = gr.Image(label="マスクプレビュー", interactive=False)

            with gr.Column(scale=2):
                images = gr.Files(label="画像をアップロード (複数可)", file_count="multiple", file_types=["image"])
                run = gr.Button("ヘッダー画像を生成")
                with gr.Row():
                    originals_gallery = gr.Gallery(label="元画像", columns=2, height=300)
                    results_gallery = gr.Gallery(label="処理結果", columns=2, height=300)
                download_zip = gr.File(label="一括ダウンロード (ZIP)")

        # Visibility and preview updates
        def toggle_inputs(ms):
            return (
                gr.update(visible=(ms == "プリセットから選択")),
                gr.update(visible=(ms == "URLから取得")),
                gr.update(visible=(ms == "ファイルをアップロード")),
            )

        mask_source.change(
            fn=toggle_inputs,
            inputs=[mask_source],
            outputs=[preset_name, mask_url, mask_upload],
            api_name="toggle_inputs",
        )

        for comp in (mask_source, preset_name, mask_url, mask_upload):
            comp.change(
                fn=update_mask_preview,
                inputs=[mask_source, preset_name, mask_url, mask_upload],
                outputs=[mask_preview],
                api_name="update_mask_preview",
            )

        run.click(
            fn=generate,
            inputs=[images, mask_source, preset_name, mask_url, mask_upload, alpha],
            outputs=[originals_gallery, results_gallery, download_zip],
            api_name="generate",
        )

    return demo


def _env_flag(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return str(val).strip().lower() in {"1", "true", "yes", "on"}


if __name__ == "__main__":
    demo = build_demo()
    demo.launch(mcp_server=_env_flag("GRADIO_MCP_SERVER", True))

def main_entry():
    """Console script entry point to launch Gradio UI."""
    demo = build_demo()
    demo.launch(mcp_server=_env_flag("GRADIO_MCP_SERVER", True))
