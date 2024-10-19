---
license: MIT
title: Pic-to-Header
sdk: Streamlit
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

Pic-to-Header is a Python application that generates header images using a mask image and an input image.

## 🚀 Features

- Upload a mask image and an input image.
- Apply the mask to the input image to generate a header image.
- Preview and download the generated header image.

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Sunwood-ai-labs/pic-to-header.git
cd pic-to-header
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 📖 Usage

1. Launch the Streamlit application:

```bash
streamlit run pic_to_header/app.py
```

2. Access the URL displayed in your browser.

3. Upload the input image and the mask image.

4. Click the "Generate Header Image" button.

5. Preview and download the generated header image as needed.


## 💻 Development

- `pic_to_header/core.py`: Contains the main image processing functions.
- `pic_to_header/app.py`: Provides the web interface using Streamlit.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```