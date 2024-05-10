import tkinter as tk
from tkinter import scrolledtext, messagebox
import numpy as np
import csv
from PIL import Image, ImageTk

def read_frequencies(filename):
    bigram_strings = []
    trigram_strings = []
    quadgram_strings = []
    bigram_frequencies = []
    trigram_frequencies = []
    quadgram_frequencies = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bigram_strings.append(row['Bigram'])
            trigram_strings.append(row['Trigram'])
            quadgram_strings.append(row['Quadgram'])
            bigram_frequencies.append(float(row['Bigram_Frequency']))
            trigram_frequencies.append(float(row['Trigram_Frequency']))
            quadgram_frequencies.append(float(row['Quadgram_Frequency']))

    return bigram_strings, trigram_strings, quadgram_strings, bigram_frequencies, trigram_frequencies, quadgram_frequencies

def load_language_data(language):
    bigram_strings, trigram_strings, quadgram_strings, frequency_bigram, frequency_trigram, frequency_quadgram = read_frequencies(f'./data/{language.lower()}.csv')
    return bigram_strings, trigram_strings, quadgram_strings, frequency_bigram, frequency_trigram, frequency_quadgram

languages = ["english", "german", "french", "spanish", "portuguese", "italian"]
language_data = {}

for language in languages:
    bigram_strings, trigram_strings, quadgram_strings, frequency_bigram, frequency_trigram, frequency_quadgram = load_language_data(language)
    language_data[language.upper()] = {
        "BIGRAM_STRINGS": bigram_strings,
        "TRIGRAM_STRINGS": trigram_strings,
        "QUADGRAM_STRINGS": quadgram_strings,
        "FREQUENCY_BIGRAM": frequency_bigram,
        "FREQUENCY_TRIGRAM": frequency_trigram,
        "FREQUENCY_QUADGRAM": frequency_quadgram
    }

languages_lower = [lang.lower() for lang in languages]

for language in languages_lower:
    frequency_bigram = language_data[language.upper()]["FREQUENCY_BIGRAM"]
    frequency_trigram = language_data[language.upper()]["FREQUENCY_TRIGRAM"]
    frequency_quadgram = language_data[language.upper()]["FREQUENCY_QUADGRAM"]
    frequency_total = frequency_bigram + frequency_trigram + frequency_quadgram
    globals()[f"frequency_{language}"] = frequency_total

def calculate_frequencies_bi(string, language):
    frequencies = [0] * len(language_data[language]["BIGRAM_STRINGS"])
    for i in range(len(string) - 1):
        bigram = string[i:i+2]
        if bigram in language_data[language]["BIGRAM_STRINGS"]:
            index = language_data[language]["BIGRAM_STRINGS"].index(bigram)
            frequencies[index] += 1
    return frequencies

def calculate_frequencies_tri(string, language):
    frequencies = [0] * len(language_data[language]["TRIGRAM_STRINGS"])
    for i in range(len(string) - 2):
        trigram = string[i:i+3]
        if trigram in language_data[language]["TRIGRAM_STRINGS"]:
            index = language_data[language]["TRIGRAM_STRINGS"].index(trigram)
            frequencies[index] += 1
    return frequencies

def calculate_frequencies_quad(string, language):
    frequencies = [0] * len(language_data[language]["QUADGRAM_STRINGS"])
    for i in range(len(string) - 3):
        quadgram = string[i:i+4]
        if quadgram in language_data[language]["QUADGRAM_STRINGS"]:
            index = language_data[language]["QUADGRAM_STRINGS"].index(quadgram)
            frequencies[index] += 1
    return frequencies

def calculate_distances(frequencies, language):
    frequency_ref = language_data[language]["FREQUENCY_BIGRAM"] + language_data[language]["FREQUENCY_TRIGRAM"] + language_data[language]["FREQUENCY_QUADGRAM"]
    distance = np.dot(frequency_ref, frequencies)
    return distance

def detect_lang(distances):
    max_distance = max(distances.values())
    language = [lang for lang, dist in distances.items() if dist == max_distance][0]
    return language

def display_language_image(language):
    if language.upper() in language_data:
        image_path = f"img/{language.lower()}.png"
        image = Image.open(image_path)
        image = ImageTk.PhotoImage(image)
        flag_label.configure(image=image)
        flag_label.image = image

def run_language_detection():
    text = text_box.get("1.0",'end-1c').strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter any text.")
        return

    filtered_text = filter_str(text)
    distances = {}

    for language in languages:
        bi_frequencies = calculate_frequencies_bi(filtered_text, language.upper())
        tri_frequencies = calculate_frequencies_tri(filtered_text, language.upper())
        quad_frequencies = calculate_frequencies_quad(filtered_text, language.upper())
        combined_frequencies = bi_frequencies + tri_frequencies + quad_frequencies
        distance = calculate_distances(combined_frequencies, language.upper())
        distances[language.upper()] = distance

        print(f"\nLanguage: {language.upper()}")
        print(f"Bigram Frequencies:")
        for i, freq in enumerate(bi_frequencies):
            bigram = language_data[language.upper()]["BIGRAM_STRINGS"][i]
            print(f"{bigram}: {freq}")

        print(f"Trigram Frequencies:")
        for i, freq in enumerate(tri_frequencies):
            trigram = language_data[language.upper()]["TRIGRAM_STRINGS"][i]
            print(f"{trigram}: {freq}")

        print(f"Quadgram Frequencies:")
        for i, freq in enumerate(quad_frequencies):
            quadgram = language_data[language.upper()]["QUADGRAM_STRINGS"][i]
            print(f"{quadgram}: {freq}")

        print(f"Distance from Reference: {distance}\n")
        
    result_text = "DISTANCES FOR EACH LANGUAGE:\n\n"
    for language, distance in distances.items():
        result_text += f"{language} : {distance:.3f}\n"

    detected_language = detect_lang(distances)

    result_text += f"\nLANGUAGE ---> {detected_language}\n\n"
    result_box.delete('1.0', tk.END)
    result_box.insert(tk.END, result_text)
    display_language_image(detected_language)

def filter_str(string):
    filtered_str = ''.join([char.upper() if char.isalpha() else ' ' for char in string])
    return filtered_str

def reset_text():
    text_box.delete('1.0', tk.END)
    result_box.delete('1.0', tk.END)
    flag_label.configure(image='')

def create_gui():
    window = tk.Tk()
    window.title("Language Detection")

    window_width = 1150
    window_height = 550
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    text_label = tk.Label(window, text="Enter Text:")
    text_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    global text_box
    text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=55, height=20)
    text_box.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    run_button = tk.Button(window, text="RUN", command=run_language_detection)
    run_button.grid(row=2, column=0, padx=200, pady=20, sticky="w")

    result_label = tk.Label(window, text="Result:")
    result_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    global result_box
    result_box = tk.Text(window, wrap=tk.WORD, width=35, height=15, highlightthickness=0, borderwidth=0)
    result_box.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    result_box.configure(bg=window.cget('bg'))

    reset_button = tk.Button(window, text="RESET", command=reset_text)
    reset_button.grid(row=2, column=1, padx=1, pady=20, sticky="e")

    global flag_label
    flag_label = tk.Label(window)
    flag_label.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="e")

    window.mainloop()

create_gui()