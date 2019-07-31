input_number1, input_number2 = map(int, input().split())
if input_number1 > input_number2:
    temp = input_number1
    input_number1 = input_number2
    input_number2 = temp


def return_len(number):
    count_list = []
    i = number
    while i != 1:
        count_list.append(i)
        if i % 2 == 0:
            i /= 2
        else:
            i = i * 3 + 1
    count_list.append(1)

    return len(count_list)


len_input_number = []
for j in range(input_number1, input_number2+1):
    len_input_number.append(return_len(j))

# print(len_input_number)
print(max(len_input_number))

