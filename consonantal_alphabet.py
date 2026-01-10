def remove_vowels(text: str) -> str:
    """Removes vowels from text."""
    vowels = "aeiouAEIOU"
    result = []

    for c in text:
        if c not in vowels:
            result.append(c)

    return "".join(result)
