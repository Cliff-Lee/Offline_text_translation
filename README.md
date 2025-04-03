# Offline Translator with Selectable Screenshot Region

This project is an offline translator for Ubuntu that lets you either translate text or take a screenshot of a selected region from your screen, perform OCR (Optical Character Recognition) to extract text, and then translate that text using offline language models from Argos Translate.

## Features

- **Text Mode:**  
  - Load text from a file or type text directly into the text area.
  
- **Offline Translation:**  
  - Translates text using Argos Translate with offline language packages.
  - Supports multiple languages. The default translation is from Chinese (`zh`) to English (`en`).

## Dependencies

This project requires:
- Python 3
- Python packages: `pytesseract`, `pyscreenshot`, `argostranslate`, and `Pillow`

## Installation

1. **Install System Dependencies:**

   Open a terminal and run:

   sudo apt update
   sudo apt install tesseract-ocr libtesseract-dev
