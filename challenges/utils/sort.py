def sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    first_half = string[:mid]
    second_half = string[mid:]

    first_sorted = sort(first_half)
    second_sorted = sort(second_half)

    return merge(first_sorted, second_sorted)


def merge(first, second):
    merged_string = ""
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged_string += first[i]
            i += 1
        else:
            merged_string += second[j]
            j += 1

    merged_string += first[i:]
    merged_string += second[j:]

    return merged_string
