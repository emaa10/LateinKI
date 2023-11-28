import os
from collections import Counter

# Funktion zum Zählen der Übereinstimmungen von Wörtern in einem Text (case-insensitiv)
def count_matches(word_list, text):
    return sum(1 for word in word_list if word.lower() in text.lower())

# Funktion zum Extrahieren von Lateinischen Wörtern aus einer Textdatei (case-insensitiv)
def extract_latin_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [word.strip().lower() for word in file.readlines()]

# Funktion zum Suchen des Briefs mit den meisten Übereinstimmungen
def find_most_matching_letter(word_list, letter_directory):
    letter_files = os.listdir(letter_directory)
    matches = {}

    for letter_file in letter_files:
        letter_path = os.path.join(letter_directory, letter_file)
        with open(letter_path, 'r', encoding='utf-8') as file:
            letter_text = file.read()
            matches[letter_file] = count_matches(word_list, letter_text)

    # Den Brief mit den meisten Übereinstimmungen finden
    most_matching_letter = max(matches, key=matches.get)
    return most_matching_letter, matches[most_matching_letter]

# Hauptfunktion
def main():
    latin_words_file = 'latin_words.txt'  # Dateipfad zur Datei mit Lateinischen Wörtern
    plinius_letters_directory = 'plinius_letters'  # Ordner mit den Plinius-Briefen

    # Lateinische Wörter extrahieren (case-insensitiv)
    latin_words = extract_latin_words(latin_words_file)

    # Den Brief mit den meisten Übereinstimmungen finden
    most_matching_letter, num_matches = find_most_matching_letter(latin_words, plinius_letters_directory)

    print(f"Der Brief mit den meisten Übereinstimmungen ist '{most_matching_letter}' mit {num_matches} Übereinstimmungen.")

if __name__ == "__main__":
    main()
