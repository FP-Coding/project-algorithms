def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if word[low_index] == word[high_index]:
        new_low = low_index + 1
        new_high = high_index - 1
        if new_low < new_high:
            return is_palindrome_recursive(word, new_low, new_high)
        else:
            return True
    else:
        return False


word = "jarara"
print(is_palindrome_recursive(word, 0, len(word) - 1))
