import csv

# read file to list
with open('resources/ex2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x in reader:
        number_list = list(map(int, x))


def operation(a, b, o):
    if o == 1:
        return a + b
    if o == 2:
        return a * b


def op(input_list, n=0):
    opcode = input_list[n]

    if opcode == 99:
        return input_list

    in1 = input_list[n + 1]
    in2 = input_list[n + 2]
    out_pos = input_list[n + 3]

    output = operation(input_list[in1], input_list[in2], opcode)

    input_list[out_pos] = output

    return op(input_list, n + 4)


# test
def test1():
    test = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    answer = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    print(op(test) == answer)


# smaller tests
def test2():
    print(op([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99])
    print(op([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99])
    print(op([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801])
    print(op([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99])


# run tests
test1()
test2()


# output
def out_put(i, j, in_list):
    new_list = in_list.copy()
    new_list[1] = i
    new_list[2] = j
    return int(op(new_list)[0])


# output 1
print(out_put(12, 2, number_list))

# output 2
x = len(number_list)
for a in range(x):
    for b in range(x):
        if out_put(a, b, number_list) == 19690720:
            print(100 * a + b)
            break
