import os
cwd = os.getcwd()


def read_file(filename):
    f = open(filename, "r")
    n = [i for i in f.read().split()]
    f.close()
    return n


def read_raw(filename):
    f = open(filename, "r")
    n = [i.rstrip('\n').rstrip('\r') for i in f.readlines()]
    f.close()
    return n


def get_testcase(test_number, read_as=read_file, folder_name='testcases'):
    i = cwd + '../{folder_name}/i{number}.txt'.format(folder_name=folder_name, number=test_number)
    o = cwd + '../{folder_name}/o{number}.txt'.format(folder_name=folder_name, number=test_number)
    return read_as(i), read_as(o)

