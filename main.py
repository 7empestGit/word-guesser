import nltk
from nltk.corpus import words

nltk.download('words')

def find_words_by_criteria(word_length: int, forbidden_letters: list, must_have_letters: list, correct_letters: dict) -> list:
    all_words:list = words.words()
    matching_words:list = []

    for word in all_words:
        if (
            len(word) == word_length
            and not any(letter in word.lower() for letter in forbidden_letters)
            and all(letter in word.lower() for letter in must_have_letters)
            and all(word[idx].lower() == char for idx, char in correct_letters.items())
            and word[0].lower() != "c"
            and word[3].lower() != "t"
            and word[5].lower() != "e"
        ):
            matching_words.append(word)

    return matching_words

def main() -> None:
    words_to_output = 10
    word_length = 6
    forbidden_letters = ["r", "s", "d", "g", "o", "l", "n"]
    must_have_letters = ["a", "t", "e", "c"]
    correct_letters = {
        0: "t",
        1: "a",
        2: "c"
    }
    matching_words = find_words_by_criteria(word_length, forbidden_letters, must_have_letters, correct_letters)

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