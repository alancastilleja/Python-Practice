
n = int(input("Input your number of elements: "))
p = int(input("Input your number of positions: "))

x = int(input("Input your number of elements: "))
y = int(input("Input your number of positions: "))

def factorial(x):
    if x == 0:
        return f'Number must be positive.'
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x > 2:
        value = x * factorial(x - 1)

    return value


def variations(n, p):
    return n ** p

def variations_no_rep(n,p):
    if n == 0 or p == 0:
        return f'use a different number'
    elif n < 0 or p < 0:
        return f'dont use negative numbers'
    elif n < p:
        return f'n must be greater than p'
    else:
        return (factorial(n)/(factorial(n - p)))

def combinations(n,p):
    if n == 0 or p == 0:
        return f'use a different number'
    elif n < 0 or p < 0:
        return f'dont use negative numbers'
    elif n < p:
        return f'n must be greater than p'
    else:
        return factorial(n) / (factorial(p)*factorial(n-p))



print('Number of variations: ' + str(variations(n, p)))
print('Number of variations with no replacement: ' + str(variations_no_rep(n, p)))
print('Number of combinations: ' + str(combinations(n, p)))

action1 = combinations(n,p)
action2 = combinations(x,y)
result = action1 * action2
print('number of combinations from seperate sample spaces ' + str(result))