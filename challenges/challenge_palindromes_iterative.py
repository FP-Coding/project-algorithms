def is_palindrome_iterative(word):
    if not word:
        return False
    reversed_string = "".join(reversed(word))
    return word == reversed_string
