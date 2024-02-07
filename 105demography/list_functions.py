def multiply_list(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] * list2[i])
    return new_list


def power_list(list, power):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] ** power)
    return new_list


def multiply_list_with_number(list, number):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] * number)
    return new_list


def add_list_with_number(list, number):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] + number)
    return new_list


def soustract_list_with_number(list, number):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] - number)
    return new_list


def divide_list_with_number(list, number):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] / number)
    return new_list


def soustract_list(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] - list2[i])
    return new_list
