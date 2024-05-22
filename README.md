# 🌐 Language Detection

This is a simple language detection application that identifies the language of the input text based on bigram, trigram, and quadgram frequencies. The project uses Tkinter for the GUI and CSV files containing n-gram frequencies for different languages.

## ✨ Features
- Detects the language of the input text.
- Supports English, German, French, Spanish, Portuguese, and Italian.
- Displays the flag of the detected language.

## 📦 Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mfurkanolcer/language-detection.git
    cd language-detection
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the required CSV files and images are in the correct directories:
    ```
    language_detection/
    ├── data/
    │   ├── english.csv
    │   ├── german.csv
    │   ├── french.csv
    │   ├── spanish.csv
    │   ├── portuguese.csv
    │   └── italian.csv
    ├── img/
    │   ├── english.png
    │   ├── german.png
    │   ├── french.png
    │   ├── spanish.png
    │   ├── portuguese.png
    │   └── italian.png
    ```

## 🚀 Usage

Run the application:
```sh
python app.py
 ```
 
## 🖼️ GUI Overview

1. **Text Input:** Enter the text you want to detect the language of.
2.  **Run Button:** Click to run the language detection algorithm.
3.  **Result Box:** Displays the detection results.
4.  **Reset Button:** Clears the input and result fields.
5.  **Language Flag:** Displays the flag of the detected language.

## 📸 Screenshots
### Main Window
![Screenshot_1](https://github.com/mfurkanolcer/nlp-project/assets/58481075/597d7430-1e8a-4680-8bfe-c9ff7c4381da)

### Detection Result
![Screenshot_2](https://github.com/mfurkanolcer/nlp-project/assets/58481075/d6b80f05-adda-4534-b649-196f02b5cb51)

## 🛠️ How It Works

1. **Reading Frequencies:** The application reads n-gram frequencies from CSV files.
2.  **Calculating Frequencies:** It calculates the frequencies of n-grams in the input text.
3.  **Calculating Distances:** It compares these frequencies with the reference frequencies from the CSV files.
4.  **Detecting Language:** The language with the highest similarity is detected and displayed.

## 📊 Data Structure

The data structure used for storing the n-gram frequencies:

```python
language_data = {
    "ENGLISH": {
        "BIGRAM_STRINGS": [...],
        "TRIGRAM_STRINGS": [...],
        "QUADGRAM_STRINGS": [...],
        "FREQUENCY_BIGRAM": [...],
        "FREQUENCY_TRIGRAM": [...],
        "FREQUENCY_QUADGRAM": [...]
    },
    ...
}
```
