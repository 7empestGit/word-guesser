# Word Guesser

### Simple word guesser for Binance's WOTD (Word Of The Day)

## Description

This is a simple Python script that helps you guess words based on specific criteria. It uses the NLTK library to access a list of words and filters them based on the length, forbidden letters, must-have letters, correct letters at specific positions, and incorrect letters at specific positions.

## Requirements

- Python 3.x
- NLTK library

You can install the required library using the following command:

```
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```
python main.py
```

You will be prompted to enter the following details:

1. Number of words to output.
2. Word length.
3. Forbidden letters (comma separated).
4. Must-have letters (comma separated).
5. Correct letters at specific positions.
6. Incorrect letters at specific positions.

The script will then output the words that match the given criteria.

## Example

```
Enter the number of words to output: 5
Enter the word length: 5
Enter forbidden letters (comma separated): a,e,i,o,u
Enter must-have letters (comma separated): t,r
Enter the index for a correct letter (or 'done' to finish): 0
Enter the letter for index 0: t
Enter the index for a correct letter (or 'done' to finish): done
Enter the index for incorrect position letters (or 'done' to finish): 1
Enter the letters for index 1 (comma separated): r
Enter the index for incorrect position letters (or 'done' to finish): done
```

The script will output the first 5 words that match the criteria.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.