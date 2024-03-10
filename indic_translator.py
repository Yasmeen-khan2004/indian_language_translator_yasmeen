import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")
        self.language_names = self.get_language_list()
        self.translator = Translator()
        self.create_widgets()

    def get_language_list(self):
        indian_languages =  ["en","hi", "bn", "gu", "kn", "km", "gom", "ml", "mni-Mtei", "mr", "ne", "or", "pa", "sa", "sd", "ta","te", "ur", "bho", "sw", "mai", "doi"] 
# Example: 1) Assamese, (2) Bengali, (3) Gujarati, (4) Hindi, (5) Kannada, (6) Kashmiri, (7) Konkani, (8) Malayalam, (9) Manipuri, (10) Marathi, (11) Nepali, (12) Oriya, (13) Punjabi, (14) Sanskrit, (15) Sindhi, (16) Tamil, (17) Telugu, (18) Urdu (19) Bodo, (20) Santhali, (21) Maithili and (22) Dogri.


        return {code: name for code, name in LANGUAGES.items() if code in indian_languages}

    def create_widgets(self):
        # Dropdown for Source Language
        self.source_language_label = tk.Label(self.root, text="Source Language:")
        self.source_language_label.grid(row=0, column=0, padx=10, pady=10)
        self.source_language_var = tk.StringVar(self.root, 'auto')  # Set default value
        self.source_language_dropdown = ttk.Combobox(self.root, textvariable=self.source_language_var, values=list(self.language_names.values()))
        self.source_language_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Dropdown for Destination Language
        self.dest_language_label = tk.Label(self.root, text="Destination Language:")
        self.dest_language_label.grid(row=1, column=0, padx=10, pady=10)
        self.dest_language_var = tk.StringVar(self.root, 'en')  # Set default value
        self.dest_language_dropdown = ttk.Combobox(self.root, textvariable=self.dest_language_var, values=list(self.language_names.values()))
        self.dest_language_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Text Entry
        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_text, width=40)
        self.entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Text to Speech Button
        self.text_to_speech_button = tk.Button(self.root, text="Text to Speech", command=self.text_to_speech)
        self.text_to_speech_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Speech to Text Button
        self.speech_to_text_button = tk.Button(self.root, text="Speech to Text", command=self.speech_to_text)
        self.speech_to_text_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Translated Text Display
        self.translation_label = tk.Label(self.root, text="")
        self.translation_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
    def translate_text(self):
        source_lang = self.source_language_var.get()
        dest_lang = self.dest_language_var.get()
        input_text = self.entry_text.get()
        translated_text = self.translator.translate(input_text, src=source_lang, dest=dest_lang)
        self.translation_label.config(text=translated_text.text)
        
    def text_to_speech(self):
        text = self.entry_text.get()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            self.entry_text.set(text)
        except Exception as e:
            print("Sorry, could not recognize your voice.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
