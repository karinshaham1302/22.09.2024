#start

numbers: list[int] = []
SENTINEL: int = 999
for i in range(10, 100 + 10, 10):
    numbers.append(i)
    if numbers == 999:
        break

# number = int(input('enter a number:'))
# numbers.insert(1, 12)
# print(numbers)

number = int(input('enter a number:'))
numbers.insert(i)
print(numbers)
