import nltk
from nltk.corpus import words

nltk.download('words')

def find_words_by_criteria(word_length, forbidden_letters, must_have_letters):
    all_words = words.words()
    matching_words = []

    for word in all_words:
        if (
            len(word) == word_length
            and not any(letter in word.lower() for letter in forbidden_letters)
            and all(letter in word.lower() for letter in must_have_letters)
            and word[1].lower() == "a"
            and word[0].lower() != "c"
            and word[3].lower() != "t"
            and word[5].lower() != "e"
        ):
            matching_words.append(word)

    return matching_words

word_length = 6
forbidden_letters = ["r", "s", "d", "g", "o", "l", "n"]
must_have_letters = ["a", "t", "e", "c"]
matching_words = find_words_by_criteria(
    word_length, forbidden_letters, must_have_letters
)

if matching_words:
    print(
        f"First 10 words with {word_length} letters, "
        f"no forbidden letters, and must contain all of '{''.join(must_have_letters)}':"
    )
    for i, word in enumerate(matching_words[:10]):
        print(f"{i+1}. {word}")
else:
    print(
        f"No words found with {word_length} letters, "
        f"no forbidden letters, and must contain all of '{''.join(must_have_letters)}'."
    )

