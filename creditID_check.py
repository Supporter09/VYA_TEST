def credit_check(id_arr):
    print(id_arr)
    if len(id_arr) %2==0:
        for i in range(0,len(id_arr)-1,2):
            id_arr[i] =id_arr[i]*2
            if id_arr[i] >9 :
                id_arr[i] -=9
    else:
        for i in range(1,len(id_arr)-1,2):
            id_arr[i] =id_arr[i]*2
            if id_arr[i] >9 :
                id_arr[i] -=9

    cc_sum=0
    print(id_arr)
    for x in id_arr:
        cc_sum+=x
    if cc_sum %10 ==0:
        return "Valid"
    else:
        return "Not VALID"
print(credit_check([3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4]))