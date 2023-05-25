def find_duplicate(nums):
    num_duplicate = False
    quantity = {}
    for num in nums:
        if num in quantity and num > 0:
            quantity[num] += 1
        else:
            quantity[num] = 1
    for num, qty in quantity.items():
        if qty > 1:
            num_duplicate = num

    return num_duplicate
