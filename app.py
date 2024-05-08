import tkinter as tk
from tkinter import scrolledtext
import numpy as np


# Dil verileri
matrix_bigram_strings = {
    "ENGLISH": ["TH", "HE", "IN", "ER", "AN", "RE", "ND", "ON", "EN", "AT",
                "OU", "ED", "HA", "TO", "OR", "IT", "IS", "HI", "ES", "NG"],
    "GERMAN": ["TH", "HE", "IN", "ER", "AN", "EN", "CH", "DE", "EI", "TE",
               "ST", "IE", "ND", "ND", "IE", "CH", "UN", "NG", "GE", "BE"],
    "ITALIAN": ["IL", "LE", "LA", "DE", "IN", "RE", "ON", "TA", "CO", "TE",
                "NT", "DI", "RE", "RE", "LI", "TI", "TA", "RA", "TO", "CA"],
    "FRENCH": ["LE", "LA", "DE", "ET", "EN", "QU", "UE", "RE", "IS", "ON",
               "NT", "NE", "RA", "SE", "NT", "RE", "TI", "UE", "UR", "IT"],
    "SPANISH": ["EL", "DE", "LA", "EN", "QU", "UE", "RE", "ER", "OS", "AR",
                "NT", "RA", "ES", "AN", "UN", "RE", "AS", "DO", "ER", "UE"],
    "PORTUGUESE": ["OS", "DE", "ES", "TE", "EM", "UE", "NT", "RA", "AS", "IS",
                    "ST", "AM", "OR", "AR", "DO", "TO", "OU", "DE", "AD", "ER"]
}

matrix_trigram_strings = {
    "ENGLISH": ["THE", "AND", "ING", "HER", "HAT", "HIS", "THA", "ERE", "FOR", "ENT",
                "ION", "TER", "WAS", "YOU", "ITH", "VER", "ALL", "WIT", "THI", "TIO"],
    "GERMAN": ["THE", "AND", "ING", "ENT", "ION", "DER", "SCH", "ICH", "NDE", "DIE",
               "GEN", "CHT", "TER", "ICH", "HTE", "DEN", "UNG", "UND", "INE", "DER"],
    "ITALIAN": ["CHE", "CON", "DEL", "PER", "DIN", "DEL", "LLE", "TER", "ELE", "ION",
                "ENT", "EST", "TTO", "ESS", "LLA", "ION", "CHE", "ION", "NDO", "IRE"],
    "FRENCH": ["LES", "QUE", "TIO", "PAR", "ION", "TRE", "RES", "ENT", "DES", "QUE",
               "DAN", "TRE", "TRE", "ONT", "ERS", "ANT", "ION", "QUE", "QUE", "EST"],
    "SPANISH": ["QUE", "EST", "LOS", "POR", "PAR", "ENT", "CON", "COM", "ARA", "DEL",
                "LOS", "PAR", "EST", "ION", "ENC", "RES", "ADA", "QUE", "SUS", "ADO"],
    "PORTUGUESE": ["QUE", "ENT", "COM", "ADO", "PAR", "DOS", "POR", "EST", "OJE", "QUE",
                    "STA", "TAM", "ORA", "ADO", "MEN", "ARA", "ARA", "ESS", "DOS", "EST"]
}

# İngilizce için güncellenmiş frekanslar
frequency_eng = [3.88, 3.68, 2.28, 2.18, 2.14,
                 1.75, 1.57, 1.42, 1.38, 1.34,
                 1.29, 1.28, 1.27, 1.17, 1.15,
                 1.13, 1.11, 1.09, 1.09, 1.05,
                 3.51, 1.59, 1.15, 0.82, 0.65,
                 0.60, 0.59, 0.56, 0.56, 0.53,
                 0.51, 0.46, 0.46, 0.44, 0.43,
                 0.43, 0.42, 0.40, 0.40, 0.38]

# Almanca için güncellenmiş frekanslar
frequency_germ = [3.88, 3.68, 2.28, 2.18, 2.14,
                  1.75, 1.57, 1.42, 1.38, 1.34,
                  1.29, 1.28, 1.27, 1.17, 1.15,
                  1.13, 1.11, 1.09, 1.09, 1.05,
                  3.51, 1.59, 1.15, 0.82, 0.65,
                  0.60, 0.59, 0.56, 0.56, 0.53,
                  0.51, 0.46, 0.46, 0.44, 0.43,
                  0.43, 0.42, 0.40, 0.40, 0.38]

# İtalyanca için güncellenmiş frekanslar
frequency_italian = [2.03, 2.03, 1.78, 1.75, 1.57,
                     1.42, 1.38, 1.34, 1.29, 1.28,
                     1.27, 1.17, 1.15, 1.13, 1.11,
                     1.09, 1.09, 1.05, 1.05, 1.03,
                     1.75, 1.59, 1.15, 0.82, 0.65,
                     0.60, 0.59, 0.56, 0.56, 0.53,
                     0.51, 0.46, 0.46, 0.44, 0.43,
                     0.43, 0.42, 0.40, 0.40, 0.38]

# Fransızca için güncellenmiş frekanslar
frequency_french = [2.03, 2.03, 1.78, 1.75, 1.57,
                    1.42, 1.38, 1.34, 1.29, 1.28,
                    1.27, 1.17, 1.15, 1.13, 1.11,
                    1.09, 1.09, 1.05, 1.05, 1.03,
                    1.75, 1.59, 1.15, 0.82, 0.65,
                    0.60, 0.59, 0.56, 0.56, 0.53,
                    0.51, 0.46, 0.46, 0.44, 0.43,
                    0.43, 0.42, 0.40, 0.40, 0.38]

# İspanyolca için güncellenmiş frekanslar
frequency_spanish = [2.03, 2.03, 1.78, 1.75, 1.57,
                     1.42, 1.38, 1.34, 1.29, 1.28,
                     1.27, 1.17, 1.15, 1.13, 1.11,
                     1.09, 1.09, 1.05, 1.05, 1.03,
                     1.75, 1.59, 1.15, 0.82, 0.65,
                     0.60, 0.59, 0.56, 0.56, 0.53,
                     0.51, 0.46, 0.46, 0.44, 0.43,
                     0.43, 0.42, 0.40, 0.40, 0.38]

# Portekizce için güncellenmiş frekanslar
frequency_portuguese = [2.03, 2.03, 1.78, 1.75, 1.57,
                         1.42, 1.38, 1.34, 1.29, 1.28,
                         1.27, 1.17, 1.15, 1.13, 1.11,
                         1.09, 1.09, 1.05, 1.05, 1.03,
                         1.75, 1.59, 1.15, 0.82, 0.65,
                         0.60, 0.59, 0.56, 0.56, 0.53,
                         0.51, 0.46, 0.46, 0.44, 0.43,
                         0.43, 0.42, 0.40, 0.40, 0.38]


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
        elif language == "SPANISH":
            frequency_ref = frequency_spanish
        elif language == "PORTUGUESE":
            frequency_ref = frequency_portuguese
        else:
            return "Language not supported!"

        distance = np.dot(frequency_ref, frequencies)
        return distance

    def detect_language(self):
        text = self.text_entry.get("1.0", tk.END)  # Tüm metni al
        filtered_text = self.filter_text(text.strip())  # Tüm metni al ve boşlukları kaldır

        distances = {}

        for language in ["ENGLISH", "GERMAN", "ITALIAN", "FRENCH", "SPANISH", "PORTUGUESE"]:
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
