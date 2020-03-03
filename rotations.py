array = [1, 2, 3, 4, 5]
n = int(input())

def rotate(l, r):
    return l[r:] + l[:r]

print(rotate(array, n))