def credit_check(id_arr):
    # Check if len(id_arr) is even or odd and apply AKA check digit
    if len(id_arr) % 2 == 0:
        for i in range(0, len(id_arr)-1, 2):
            id_arr[i] = id_arr[i]*2
            if id_arr[i] > 9:
                id_arr[i] -= 9
    else:
        for i in range(1, len(id_arr)-1, 2):
            id_arr[i] = id_arr[i]*2
            if id_arr[i] > 9:
                id_arr[i] -= 9
    # Sum up all the credit number in the credit card
    cc_sum = 0
    for x in id_arr:
        cc_sum += x
    # Validate the number
    if cc_sum % 10 == 0:
        return "Valid"
    else:
        return "Not VALID"


id_arr = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6]
# Điền các số credit card của bạn vào trong dưới dạng một list vao trong id_arr
# Ví dụ: id_arr =[3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6]
print(credit_check(id_arr))
