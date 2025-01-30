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
    words_to_output = 10
    word_length = 7
    forbidden_letters = {"d", "a", "g", "s"}
    must_have_letters = {"r", "o", "n"}
    correct_letters = {
        5: "n"
    }
    incorrect_position_letters = {
        1: ["i", "r"],
        4: ["n", "i"]
    }
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