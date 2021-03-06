'''
    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
'''

sum = 0
t1 = 0
t2 = 1
for num in range(2, 4000000):
    t = t1 + t2
    if num > t:
        t1 = t2
        t2 = t
    elif num == t and num % 2 == 0:
        sum += num

print("Sum of all even Fibonacci terms, less than 4000000 = %d" %sum)
