import tkinter as tk
from tkinter import scrolledtext
import numpy as np

# Dil verileri
matrix_bigram_strings = {
    "ENGLISH": ["TH", "HE", "IN", "ER", "AN", "EN", "CH", "DE", "EI", "TE"],
    "GERMAN": ["TH", "HE", "IN", "ER", "AN", "EN", "CH", "DE", "EI", "TE"],
    "ITALIAN": ["IL", "LE", "LA", "DE", "IN", "RE", "ON", "TA", "CO", "TE"],
    "FRENCH": ["LE", "LA", "DE", "ET", "EN", "QU", "UE", "RE", "IS", "ON"]
}

matrix_trigram_strings = {
    "ENGLISH": ["THE", "AND", "ING", "ENT", "ION", "DER", "SCH", "ICH", "NDE", "DIE"],
    "GERMAN": ["THE", "AND", "ING", "ENT", "ION", "DER", "SCH", "ICH", "NDE", "DIE"],
    "ITALIAN": ["CHE", "CON", "DEL", "PER", "DIN", "DEL", "LLE", "TER", "ELE", "ION"],
    "FRENCH": ["LES", "QUE", "TIO", "PAR", "ION", "TRE", "RES", "ENT", "DES", "QUE"]
}

frequency_eng = [2.71, 2.33, 2.03, 1.78, 1.61,
                 1.13, 0.01, 0.01, 0.01, 0.01,
                 1.81, 0.73, 0.72, 0.42, 0.42,
                 0.01, 0.01, 0.01, 0.01, 0.01]

frequency_germ = [0.01, 0.89, 1.71, 3.90, 1.07,
                  3.61, 2.36, 2.31, 1.98, 1.98,
                  0.01, 0.01, 0.01, 0.01, 0.01,
                  1.04, 0.76, 0.75, 0.72, 0.62]

frequency_italian = [2.96, 0.96, 1.55, 1.18, 1.17,
                     0.94, 0.93, 0.92, 0.88, 0.82,
                     0.71, 0.62, 0.62, 0.55, 0.54,
                     0.53, 0.53, 0.53, 0.51, 0.50]

frequency_french = [3.77, 2.51, 2.11, 2.09, 2.01,
                    1.79, 1.68, 1.66, 1.64, 1.36,
                    1.32, 1.22, 1.05, 0.98, 0.95,
                    0.93, 0.91, 0.85, 0.84, 0.83]

class LanguageDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Detector")

        self.create_widgets()

    def create_widgets(self):
        # Metin girişi için etiket ve metin kutusu
        self.text_label = tk.Label(self.root, text="Enter Text:")
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.text_entry = scrolledtext.ScrolledText(self.root, width=40, height=10, wrap=tk.WORD)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Dil tespiti için buton
        self.detect_button = tk.Button(self.root, text="Detect Language", command=self.detect_language)
        self.detect_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Bigram ve trigram sonuçlarını göstermek için etiketler
        self.bigram_label = tk.Label(self.root, text="Bigram Frequencies:")
        self.bigram_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.trigram_label = tk.Label(self.root, text="Trigram Frequencies:")
        self.trigram_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.bigram_output = scrolledtext.ScrolledText(self.root, width=20, height=10, wrap=tk.WORD)
        self.bigram_output.grid(row=3, column=0, padx=10, pady=10)

        self.trigram_output = scrolledtext.ScrolledText(self.root, width=20, height=10, wrap=tk.WORD)
        self.trigram_output.grid(row=3, column=1, padx=10, pady=10)

        # Dil tespiti sonucunu göstermek için etiket
        self.output_label = tk.Label(self.root, text="", wraplength=300, justify="left")
        self.output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def filter_text(self, text):
        filtered_text = ''.join([char.upper() if char.isalpha() else ' ' for char in text])
        return filtered_text

    def calculate_frequencies_bi(self, string, language):
        frequencies = [0] * len(matrix_bigram_strings[language])
        for i in range(len(string) - 1):
            bigram = string[i:i+2]
            if bigram in matrix_bigram_strings[language]:
                index = matrix_bigram_strings[language].index(bigram)
                frequencies[index] += 1
        return frequencies

    def calculate_frequencies_tri(self, string, language):
        frequencies = [0] * len(matrix_trigram_strings[language])
        for i in range(len(string) - 2):
            trigram = string[i:i+3]
            if trigram in matrix_trigram_strings[language]:
                index = matrix_trigram_strings[language].index(trigram)
                frequencies[index] += 1
        return frequencies

    def calculate_distances(self, frequencies, language):
        if language == "ENGLISH":
            frequency_ref = frequency_eng
        elif language == "GERMAN":
            frequency_ref = frequency_germ
        elif language == "ITALIAN":
            frequency_ref = frequency_italian
        elif language == "FRENCH":
            frequency_ref = frequency_french
        else:
            return "Language not supported!"

        distance = np.dot(frequency_ref, frequencies)
        return distance

    def detect_language(self):
        text = self.text_entry.get("1.0", tk.END)
        filtered_text = self.filter_text(text)

        distances = {}

        for language in ["ENGLISH", "GERMAN", "ITALIAN", "FRENCH"]:
            bi_frequencies = self.calculate_frequencies_bi(filtered_text, language)
            tri_frequencies = self.calculate_frequencies_tri(filtered_text, language)
            combined_frequencies = bi_frequencies + tri_frequencies
            distance = self.calculate_distances(combined_frequencies, language)
            distances[language] = distance

        max_distance = max(distances.values())
        detected_language = [lang for lang, dist in distances.items() if dist == max_distance][0]

        # Bigram ve trigram sonuçlarını güncelle
        self.bigram_output.delete('1.0', tk.END)
        self.trigram_output.delete('1.0', tk.END)

        for lang, bi_freq in matrix_bigram_strings.items():
            if lang == detected_language:
                self.bigram_output.insert(tk.END, f"{lang}:\n")
                for bi, freq in zip(bi_freq, bi_frequencies):
                    self.bigram_output.insert(tk.END, f"{bi} : {freq}\n")
            else:
                self.bigram_output.insert(tk.END, f"{lang}: Not Detected\n")

        for lang, tri_freq in matrix_trigram_strings.items():
            if lang == detected_language:
                self.trigram_output.insert(tk.END, f"{lang}:\n")
                for tri, freq in zip(tri_freq, tri_frequencies):
                    self.trigram_output.insert(tk.END, f"{tri} : {freq}\n")
            else:
                self.trigram_output.insert(tk.END, f"{lang}: Not Detected\n")

        # Dil tespiti sonucunu güncelle
        self.output_label.config(text=f"Detected Language: {detected_language}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()
    
    
