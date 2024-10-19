---
license: mit
title: pic-to-header
sdk: streamlit
emoji: 🐨
colorFrom: blue
colorTo: purple
pinned: false
app_file: pic_to_header/app.py
---

<div align="center">

# Pic-to-Header

![Pic-to-Header Result](https://raw.githubusercontent.com/Sunwood-ai-labs/pic-to-header/refs/heads/main/assets/result.png)

[![GitHub license](https://img.shields.io/github/license/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/issues)
[![GitHub release](https://img.shields.io/github/release/Sunwood-ai-labs/pic-to-header.svg)](https://GitHub.com/Sunwood-ai-labs/pic-to-header/releases/)
[![GitHub tag](https://img.shields.io/github/tag/Sunwood-ai-labs/pic-to-header.svg)](https://GitHub.com/Sunwood-ai-labs/pic-to-header/tags/)
[![PyPI version](https://badge.fury.io/py/pic-to-header.svg)](https://badge.fury.io/py/pic-to-header)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

</div>

Pic-to-Headerは、マスク画像と入力画像を使用してヘッダー画像を生成するPythonアプリケーションです。 バージョン 0.1.1 がリリースされました。

## 🚀 プロジェクト概要

Pic-to-Headerは、マスク画像と入力画像を使用して簡単にヘッダー画像を生成し、ダウンロードできるStreamlitアプリケーションです。PyPIにも公開されています。  コマンドラインインターフェース(CLI)にも対応しています。

## ✨ 主な機能

- マスク画像と入力画像のアップロード
- ヘッダー画像の生成
- 生成されたヘッダー画像のプレビューとダウンロード
- コマンドラインインターフェース (CLI) を使用した画像処理
- READMEページとリリースノートページのStreamlitアプリへの追加


## 🔧 使用方法

### 方法1: PyPIからのインストール

Pic-to-Headerは、PyPIで利用可能です。以下のコマンドでインストールできます：

```bash
pip install pic-to-header
```

### 方法2: ソースからのインストール

1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/Sunwood-ai-labs/pic-to-header.git
   cd pic-to-header
   ```
2. 必要な依存関係をインストールします:
   ```bash
   pip install -r requirements.txt
   ```

### Streamlitウェブアプリケーション

1. Streamlitアプリケーションを起動します：
   ```bash
   streamlit run pic_to_header/app.py
   ```
2. ブラウザで表示されるURLにアクセスします。
3. 入力画像とマスク画像をアップロードします。
4. "ヘッダー画像を生成"ボタンをクリックします。
5. 生成されたヘッダー画像をプレビューし、必要に応じてダウンロードします。


### コマンドラインインターフェース (CLI)

CLIを使用して画像を処理することもできます：

```bash
pic-to-header input_image.png mask_image.png output_image.png
```

例：

```bash
pic-to-header assets/sample.png assets/mask.png output_image.png
```


## 📦 インストール手順

上記「使用方法」セクションを参照してください。


## 🆕 最新情報

- コマンドラインインターフェース(CLI)の実装により、コマンドラインから画像処理が可能になりました。
- READMEページとリリースノートページがStreamlitアプリに追加されました。
- ドキュメントが改善され、PyPIからのインストール方法やCLIの使い方などが追加されました。
- CLIのエントリポイントが`pic_to_header.app:main`から`pic_to_header.cli:main`に変更されました。
- バージョン番号が0.1.0から0.1.1に更新されました。


## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。