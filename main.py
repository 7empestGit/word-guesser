import nltk
from nltk.corpus import words

nltk.download('words')

def find_words_by_criteria(word_length: int, forbidden_letters: set, must_have_letters: set, correct_letters: dict, incorrect_position_letters: dict) -> list:
    all_words = words.words()
    matching_words = []

    for word in all_words:
        word_lower = word.lower()
        if len(word) != word_length: 
            continue
        
        if any(letter in word_lower for letter in forbidden_letters):
            continue
        
        if not must_have_letters.issubset(word_lower):
            continue
        
        if any(word_lower[idx] != char for idx, char in correct_letters.items()):
            continue
        
        if any(word_lower[idx] in chars for idx, chars in incorrect_position_letters.items()):
            continue
        
        matching_words.append(word)

    return matching_words

def main() -> None:
    words_to_output = int(input("Enter the number of words to output: "))
    word_length = int(input("Enter the word length: "))
    forbidden_letters = set(input("Enter forbidden letters (comma separated): ").split(","))
    must_have_letters = set(input("Enter must-have letters (comma separated): ").split(","))
    
    correct_letters = {}
    while True:
        idx = input("Enter the index for a correct letter (or 'done' to finish): ")
        if idx.lower() == 'done':
            break
        letter = input(f"Enter the letter for index {idx}: ")
        correct_letters[int(idx)] = letter
    
    incorrect_position_letters = {}
    while True:
        idx = input("Enter the index for incorrect position letters (or 'done' to finish): ")
        if idx.lower() == 'done':
            break
        letters = input(f"Enter the letters for index {idx} (comma separated): ").split(",")
        incorrect_position_letters[int(idx)] = letters

    matching_words = find_words_by_criteria(word_length, forbidden_letters, must_have_letters, correct_letters, incorrect_position_letters)

    if matching_words:
        print(
            f"First {words_to_output} words with {word_length} letters, "
            f"no forbidden letters, and must contain all of '{''.join(must_have_letters)}':"
        )
        for i, word in enumerate(matching_words[:words_to_output]):
            print(f"{i+1}. {word}")
    else:
        print(
            f"No words found with {word_length} letters, "
            f"no forbidden letters, and must contain all of '{''.join(must_have_letters)}'."
        )

if __name__ == "__main__":
    main()