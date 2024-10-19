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

Pic-to-Header is a Python application that generates header images using a mask image and an input image. Version 0.1.1 has been released.

## 🚀 Project Overview

Pic-to-Header is a Streamlit application that allows you to easily generate and download header images using a mask image and an input image. It's also available on PyPI.  It also supports a command-line interface (CLI).

## ✨ Key Features

- Upload mask and input images
- Generate header images
- Preview and download generated header images
- Image processing using a command-line interface (CLI)
- Added README page and release notes page to the Streamlit app


## 🔧 Usage

### Method 1: Installation from PyPI

Pic-to-Header is available on PyPI.  You can install it using the following command:

```bash
pip install pic-to-header
```

### Method 2: Installation from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/Sunwood-ai-labs/pic-to-header.git
   cd pic-to-header
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Streamlit Web Application

1. Start the Streamlit application:
   ```bash
   streamlit run pic_to_header/app.py
   ```
2. Access the URL displayed in your browser.
3. Upload your input and mask images.
4. Click the "Generate Header Image" button.
5. Preview and download the generated header image as needed.


### Command-Line Interface (CLI)

You can also process images using the CLI:

```bash
pic-to-header input_image.png mask_image.png output_image.png
```

Example:

```bash
pic-to-header assets/sample.png assets/mask.png output_image.png
```

### Using the Python Script

The `pic-to-header` package can also be used directly within a Python script.  Here's an example:

```python
from pic_to_header.core import process_header_image

# Specify the paths to the input image, mask image, and output image
input_image_path = "path/to/input_image.png"
mask_image_path = "path/to/mask_image.png"
output_image_path = "path/to/output_image.png"

# Generate the header image
result = process_header_image(input_image_path, mask_image_path, output_image_path)

print(f"Header image generated: {result}")
```

This script works as follows:

1. Imports the `process_header_image` function from the `pic_to_header.core` module.
2. Specifies the paths to the input image, mask image, and output image.
3. Calls the `process_header_image` function to generate the header image.
4. Displays the path to the generated image.

Running this script will generate the header image at the specified output path.

## 💻 Development

- `pic_to_header/core.py`: Contains the core image processing functionality.
- `pic_to_header/app.py`: Provides the web interface using Streamlit.
- `pic_to_header/cli.py`: Provides the command-line interface.


## 📦 Installation Instructions

See the "Usage" section above.


## 🆕 What's New

- Implemented a command-line interface (CLI) for image processing from the command line.
- Added a README page and release notes page to the Streamlit app.
- Improved documentation, adding instructions for installation from PyPI and CLI usage.
- Changed the CLI entry point from `pic_to_header.app:main` to `pic_to_header.cli:main`.
- Version number updated from 0.1.0 to 0.1.1.


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.