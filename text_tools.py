from consonantal_alphabet import remove_vowels

def main():
    text = input("Enter a text: ")

    print("Word count:", count_words(text))
    print("Letter count:", count_letters(text))
    print("Count of 'a':", count_specific_letter(text, 'a'))
    print("Reverse text:", reverse_text(text))


def count_words(text: str)-> int:
    """Counts the nuber of words in a text, using Python's built-in split()."""
    return len(text.split())

def count_letters(text: str) -> int:
    """Counts nuber of letters (including spaces)."""
    return len(text)

def count_specific_letter(text: str, letter: str) -> int:
    """Counts how often a letter appears in a text."""
    return text.count(letter)

def reverse_text(text: str) -> str:
    """Reverses the given text."""
    return text[::-1]

if __name__ == '__main__':
    main()