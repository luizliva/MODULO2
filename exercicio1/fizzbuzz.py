"""
Fizz Buzz
"""

def fb(n):
    if n % 3 == 0 and n % 5 ==0:
        return 'Fizz Buzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n

print(fb(4))
print(fb(6))
print(fb(15))
print(fb(10))
