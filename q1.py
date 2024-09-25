# start

my_list: list[int] = []
for i in range(1, 100 + 1):
    my_list.append(i)

print('the first number', my_list[0])
print('the last number', my_list[-1])
print('all the numbers', my_list[:len(my_list)])  # --->  my_list[:])
print('the numbers 3-12', my_list[2:12])
print('the numbers 80-100', my_list[79:])
print('all the number until 17', my_list[:17])
print('in reverse order', my_list[-1:-101:-1])
print('the even numbers', my_list[1::2])
print('the number that divide by 3', my_list[2::3])
print('the number that divide by 7', my_list[6::7])
print('the numbers that multiples of 10', my_list[9::10])
print('the numbers 99-66 in skips of three', my_list[-2:63:-3])

my_list.insert(50, 999)
print('number 999 in the center:', my_list)

my_list.pop()
print('without the lest number:', my_list)

# stop
