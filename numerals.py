# def numerus (roman):
#     i=1
#     v=5
#     x=10
#     l=50
#     c=100
#     m=1000
#     p = p
#     for r in roman:
#         p = print (p+r)
#     return p

# numerus (x)

#

def to_val(n):
    if n == 'i': return 1
    elif n =='v': return 5
    elif n == 'x': return 10
    elif n == 'c': return 100
    elif n == 'm': return 1000
    return 0

def numurus (roman):
    total = 0
    prev = 0
    for letter in roman:
        cur = to_val(letter)
        if prev < cur:
            total -= prev
            cur -= prev
        total += cur
        prev = cur
    print (total)

numurus ('xiv')       
    