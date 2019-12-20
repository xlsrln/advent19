import numpy as np
import csv

start_pos = (5000, 5000)

def tuple_add(tup, v, h):
    return tup[0] + v, tup[1] + h


def cable_put(arr, pos):
    arr[pos[0]][pos[1]] += 1


def read_instruction(code, pos, ar):

    #print(pos)
    it = int(code[1])

    if it == 0:
        return code, pos

    if code[0] == 'U':
        (v, h) = (1, 0)
    if code[0] == 'D':
        (v, h) = (-1, 0)
    if code[0] == 'R':
        (v, h) = (0, 1)
    if code[0] == 'L':
        (v, h) = (0, -1)

    new_pos = tuple_add(pos, v, h)
    new_code = code[0] + str(it - 1)

    cable_put(ar, new_pos)

    return read_instruction(new_code, new_pos, ar)


def read_list(code_list, pos=start_pos, ar=None):
    if len(code_list) < 1:
        return ar
    else:
        code = code_list[0]
        (_, pos) = read_instruction(code, pos, ar)
        read_list(code_list[1:], pos, ar)


a = np.zeros((10, 10))
b = np.zeros((10, 10))

read_list('R8,U5,L5,D3'.split(sep=','), (0, 0), a)
read_list('U7,R6,D4,L4'.split(sep=','), (0, 0), b)

print(a)
print(b)

a = a.clip(max=1)
b = b.clip(max=1)

x = np.add(a, b)

print(x)

print(np.where(x == 2)[1])

if False:
    # read file to list
    with open("resources/ex3.csv", "r") as file:

        c = np.zeros((10000, 10000))
        d = np.zeros((10000, 10000))

        input1 = file.readline().split(',')
        input2 = file.readline().split(',')

        #print(input1)

        read_list(input1, ar=c)
        read_list(input1, ar=d)

        c = c.clip(max=1)
        d = d.clip(max=1)

        e = np.add(c, d)
        print(np.where(e == 2))
