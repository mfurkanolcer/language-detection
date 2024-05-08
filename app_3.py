# Her dil icin bigram ve brigram skorlarini da yazdirir

import numpy as np
import csv

def read_frequencies(filename):
    bigram_strings = []
    trigram_strings = []
    bigram_frequencies = []
    trigram_frequencies = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bigram_strings.append(row['Bigram'])
            trigram_strings.append(row['Trigram'])
            bigram_frequencies.append(float(row['Bigram_Frequency']))
            trigram_frequencies.append(float(row['Trigram_Frequency']))

    return bigram_strings, trigram_strings, bigram_frequencies, trigram_frequencies

english_bigram_strings, english_trigram_strings, frequency_eng_bigram, frequency_eng_trigram = read_frequencies('./csv/english.csv')
german_bigram_strings, german_trigram_strings, frequency_germ_bigram, frequency_germ_trigram = read_frequencies('./csv/german.csv')
french_bigram_strings, french_trigram_strings, frequency_french_bigram, frequency_french_trigram = read_frequencies('./csv/french.csv')
spanish_bigram_strings, spanish_trigram_strings, frequency_spanish_bigram, frequency_spanish_trigram = read_frequencies('./csv/spanish.csv')
portuguese_bigram_strings, portuguese_trigram_strings, frequency_portuguese_bigram, frequency_portuguese_trigram = read_frequencies('./csv/portuguese.csv')
italian_bigram_strings, italian_trigram_strings, frequency_italian_bigram, frequency_italian_trigram = read_frequencies('./csv/italian.csv')
turkish_bigram_strings, turkish_trigram_strings, frequency_turkish_bigram, frequency_turkish_trigram = read_frequencies('./csv/turkish.csv')

matrix_bigram_strings = {
    "ENGLISH": english_bigram_strings,
    "GERMAN": german_bigram_strings,
    "FRENCH": french_bigram_strings,
    "SPANISH": spanish_bigram_strings,
    "PORTUGUESE": portuguese_bigram_strings,
    "ITALIAN": italian_bigram_strings,
    "TURKISH": turkish_bigram_strings
}

matrix_trigram_strings = {
    "ENGLISH": english_trigram_strings,
    "GERMAN": german_trigram_strings,
    "FRENCH": french_trigram_strings,
    "SPANISH": spanish_trigram_strings,
    "PORTUGUESE": portuguese_trigram_strings,
    "ITALIAN": italian_trigram_strings,
    "TURKISH": turkish_bigram_strings
}

frequency_eng = frequency_eng_bigram + frequency_eng_trigram
frequency_germ = frequency_germ_bigram + frequency_germ_trigram
frequency_french = frequency_french_bigram + frequency_french_trigram
frequency_spanish = frequency_spanish_bigram + frequency_spanish_trigram
frequency_portuguese = frequency_portuguese_bigram + frequency_portuguese_trigram
frequency_italian = frequency_italian_bigram + frequency_italian_trigram
frequency_turkish = frequency_turkish_bigram + frequency_turkish_trigram

def filter_str(string):
    filtered_str = ''.join([char.upper() if char.isalpha() else ' ' for char in string])
    print(filtered_str)
    print("\n*************************\n")
    return filtered_str

def calculate_frequencies_bi(string, language):
    frequencies = [0] * len(matrix_bigram_strings[language])
    for i in range(len(string) - 1):
        bigram = string[i:i+2]
        if bigram in matrix_bigram_strings[language]:
            index = matrix_bigram_strings[language].index(bigram)
            frequencies[index] += 1
    print("\n\tBIGRAM\n\n")
    for bigram, frequency in zip(matrix_bigram_strings[language], frequencies):
        print(f"{bigram} : {frequency:.2f}")
    print("\n*************************\n\n")
    return frequencies

def calculate_frequencies_tri(string, language):
    frequencies = [0] * len(matrix_trigram_strings[language])
    for i in range(len(string) - 2):
        trigram = string[i:i+3]
        if trigram in matrix_trigram_strings[language]:
            index = matrix_trigram_strings[language].index(trigram)
            frequencies[index] += 1
    print("\tTRIGRAM\n\n")
    for trigram, frequency in zip(matrix_trigram_strings[language], frequencies):
        print(f"{trigram} : {frequency:.2f}")
    print("\n*************************\n")
    return frequencies

def calculate_distances(frequencies, language):
    if language == "ENGLISH":
        frequency_ref = frequency_eng
    elif language == "GERMAN":
        frequency_ref = frequency_germ
    elif language == "FRENCH":
        frequency_ref = frequency_french
    elif language == "SPANISH":
        frequency_ref = frequency_spanish
    elif language == "PORTUGUESE":
        frequency_ref = frequency_portuguese
    elif language == "ITALIAN":
        frequency_ref = frequency_italian
    elif language == "TURKISH":
        frequency_ref = frequency_turkish
    else:
        print("Language not supported!")
        return

    distance = np.dot(frequency_ref, frequencies)
    print(f"\n\tCALCULATED FREQUENCIES for {language}\n\n")
    print(f"{language} : {distance:.3f}\n")
    print("\n**************************\n\n")
    return distance

def detect_lang(distances):
    max_distance = max(distances.values())
    language = [lang for lang, dist in distances.items() if dist == max_distance][0]
    print(f"LANGUAGE ---> {language}\n")
    print("\n**************************\n")

def main():
    text = input("TEXT:\n\n")
    print("\n**************************")
    print("\n\nFILTERED TEXT:\n\n")
    filtered_text = filter_str(text)

    distances = {}

    for language in ["ENGLISH", "GERMAN", "FRENCH", "SPANISH", "PORTUGUESE", "ITALIAN", "TURKISH"]:
        bi_frequencies = calculate_frequencies_bi(filtered_text, language)
        tri_frequencies = calculate_frequencies_tri(filtered_text, language)
        combined_frequencies = bi_frequencies + tri_frequencies
        distance = calculate_distances(combined_frequencies, language)
        distances[language] = distance

    print("\n**************************")
    print("\nDISTANCES FOR EACH LANGUAGE:\n")
    for language, distance in distances.items():
        print(f"{language} : {distance:.3f}")
    print("\n**************************\n")

    detect_lang(distances)

if __name__ == "__main__":
    main()