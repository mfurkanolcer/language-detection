import numpy as np

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
    elif language == "ITALIAN":
        frequency_ref = frequency_italian
    elif language == "FRENCH":
        frequency_ref = frequency_french
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

    for language in ["ENGLISH", "GERMAN", "ITALIAN", "FRENCH"]:
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