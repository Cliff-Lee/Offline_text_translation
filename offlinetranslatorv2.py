#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pytesseract
from PIL import Image
from argostranslate import translate

def extract_text_from_image(image_path):
    """Extract text from an image using pytesseract."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def translate_text(text, from_lang_code, to_lang_code):
    """Translate text using Argos Translate. Make sure the language packages are installed."""
    installed_languages = translate.load_installed_languages()
    from_lang = next((lang for lang in installed_languages if lang.code == from_lang_code), None)
    to_lang = next((lang for lang in installed_languages if lang.code == to_lang_code), None)
    if not from_lang or not to_lang:
        raise Exception("Language package not installed. Install the package for your selected language pair.")
    translation = from_lang.get_translation(to_lang)
    return translation.translate(text)

def select_file():
    """Open a file dialog to load a text file."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, f.read())
# Extended list of languages (add more language codes as needed)
languages = [
    "en",  # English
    "es",  # Spanish
    "fr",  # French
    "de",  # German
    "it",  # Italian
    "pt",  # Portuguese
    "ru",  # Russian
    "zh",  # Chinese
    "ja",  # Japanese
    "ko",  # Korean
    "ar",  # Arabic
    "hi",  # Hindi
    "nl",  # Dutch
    "sv",  # Swedish
    "pl",  # Polish
    "tr",  # Turkish
    # Add more language codes as needed
]

def translate_action():
    """Translate the text entered in the text mode and display the result."""
    try:
        from_lang = from_lang_combo.get()
        to_lang = to_lang_combo.get()
        text = text_input.get("1.0", tk.END)
        if not text.strip():
            messagebox.showwarning("Warning", "No text found to translate.")
            return
        result = translate_text(text, from_lang, to_lang)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Build the GUI using Tkinter
root = tk.Tk()
root.title("Offline Translator")

# Input text area for text mode
frame_text = ttk.LabelFrame(root, text="Input Text")
frame_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
text_input = tk.Text(frame_text, width=60, height=10)
text_input.pack(side="left", fill="both", expand=True)
scrollbar = ttk.Scrollbar(frame_text, command=text_input.yview)
scrollbar.pack(side="right", fill="y")
text_input.config(yscrollcommand=scrollbar.set)

# Button to load a text file
btn_load = ttk.Button(root, text="Load Text File", command=select_file)
btn_load.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Language selection dropdowns with defaults: from Chinese (zh) to English (en)
frame_lang = ttk.Frame(root)
frame_lang.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
ttk.Label(frame_lang, text="From:").grid(row=0, column=0, padx=5, pady=5)
from_lang_combo = ttk.Combobox(frame_lang, values=languages, state="readonly", width=5)
from_default_index = languages.index("zh") if "zh" in languages else 0
from_lang_combo.current(from_default_index)
from_lang_combo.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(frame_lang, text="To:").grid(row=0, column=2, padx=5, pady=5)
to_lang_combo = ttk.Combobox(frame_lang, values=languages, state="readonly", width=5)
to_default_index = languages.index("en") if "en" in languages else 0
to_lang_combo.current(to_default_index)
to_lang_combo.grid(row=0, column=3, padx=5, pady=5)

# Translate button
btn_translate = ttk.Button(root, text="Translate", command=translate_action)
btn_translate.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Output area for translated text
frame_result = ttk.LabelFrame(root, text="Translated Text")
frame_result.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
result_text = tk.Text(frame_result, width=60, height=10)
result_text.pack(side="left", fill="both", expand=True)
scrollbar2 = ttk.Scrollbar(frame_result, command=result_text.yview)
scrollbar2.pack(side="right", fill="y")
result_text.config(yscrollcommand=scrollbar2.set)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(4, weight=1)

root.mainloop()

