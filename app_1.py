# Direk hangi dil oldugunu yazar

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

def read_language_data(language):
    bigram_strings, trigram_strings, frequency_bigram, frequency_trigram = read_frequencies(f'./csv/{language}.csv')
    return bigram_strings, trigram_strings, frequency_bigram, frequency_trigram

languages = ['english', 'german', 'french', 'spanish', 'portuguese', 'italian', 'turkish']
data = {}

for language in languages:
    data[language] = read_language_data(language)

def filter_string(string):
    return ''.join([char.upper() if char.isalpha() else ' ' for char in string])

def calculate_frequencies(ngram_strings, frequencies, string):
    ngram_frequencies = [0] * len(ngram_strings)
    for i in range(len(string) - len(ngram_strings[0]) + 1):
        ngram = string[i:i+len(ngram_strings[0])]
        if ngram in ngram_strings:
            index = ngram_strings.index(ngram)
            ngram_frequencies[index] += 1
    return ngram_frequencies

def calculate_distances(language, frequencies):
    frequency_ref = data[language][2] + data[language][3]
    return np.dot(frequency_ref, frequencies)

def detect_language(distances):
    max_distance = max(distances.values())
    return [lang for lang, dist in distances.items() if dist == max_distance][0]

def main():
    text = input("\nTEXT:\n")
    filtered_text = filter_string(text)

    distances = {}

    for language in languages:
        bi_frequencies = calculate_frequencies(data[language][0], data[language][2], filtered_text)
        tri_frequencies = calculate_frequencies(data[language][1], data[language][3], filtered_text)
        combined_frequencies = bi_frequencies + tri_frequencies
        distances[language] = calculate_distances(language, combined_frequencies)

    detected_language = detect_language(distances)

    print("\n")
    print(f"LANGUAGE:\n{detected_language.upper()}\n")

if __name__ == "__main__":
    main()