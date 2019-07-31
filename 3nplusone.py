input_number = 3

count_list = [i for i in range(input_number + 1)]


def return_len(number):
    count_list[number] = []
    i = number
    while i != 1:
        count_list[number].append(i)
        if i % 2 == 0:
            i /= 2
        else:
            i = i * 3 + 1
    count_list[number].append(1)

    return len(count_list[input_number])


len_input_number = return_len(input_number)
print(len_input_number)
print("hello")