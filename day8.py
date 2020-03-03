integer = int(input())
names_and_numbers = [input().split() for _ in range(integer)]
phone_book = {k: v for k, v in names_and_numbers}

for _ in range(integer):
    name = str(input())
    if name in phone_book:
        print(name + '=' + phone_book[name])
    else:
        print("Not found")


