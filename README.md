# Pic-to-Header

Pic-to-Headerは、マスク画像と入力画像を使用してヘッダー画像を生成するPythonアプリケーションです。

## 機能

- マスク画像と入力画像をアップロード
- 入力画像にマスクを適用してヘッダー画像を生成
- 生成されたヘッダー画像のプレビューとダウンロード

## インストール

1. リポジトリをクローンします：

```
git clone https://github.com/yourusername/pic-to-header.git
cd pic-to-header
```

2. 必要な依存関係をインストールします：

```
pip install -r requirements.txt
```

## 使用方法

1. Streamlitアプリケーションを起動します：

```
streamlit run web_app/app.py
```

2. ブラウザで表示されるURLにアクセスします。

3. 入力画像とマスク画像をアップロードします。

4. "ヘッダー画像を生成"ボタンをクリックします。

5. 生成されたヘッダー画像をプレビューし、必要に応じてダウンロードします。

## 開発

- `pic_to_header/core.py`: 画像処理の主要な機能を含みます。
- `web_app/app.py`: Streamlitを使用したWebインターフェースを提供します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
