'''def even(a):
    if a % 2 == 0:
        return a
    
def even_sum(n):
    j = 0
    for i in range(1, n):
        if i % 2 == 0:
            j += i
    return j
'''
def even(a):
    if a % 2 == 0:
        return 1

def even_sum(a):
    j = 0
    for i in range(1, a+1):
        if even(i) == True:
            j += i
    return j
    

n = int(input("범위 시작의 양수 n: "))
m = int(input("범위 끝의 양수 m: "))

print(even_sum(m) - even_sum(n))

#풀어야함
