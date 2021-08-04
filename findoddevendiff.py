def evenodddiff(arr, n):
    even_sum = 0
    odd_sum = 0
    for i in arr:
        if not i % 2:
            odd_sum += i
        else:
            even_sum += i

    diff = abs(even_sum - odd_sum)
    print(diff)

arr = [10, 11, 7, 12, 14]
n = len(arr)
evenodddiff(arr, n)