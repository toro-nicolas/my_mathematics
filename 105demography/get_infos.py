import csv


def get_data_from_csv():
    data = []
    try:
        with open("105demography_data.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                data.append(row)
        return data
    except:
        print("Error with the file")
        exit(84)


def print_country(country_list):
    print("Country: ", end="")
    for i in range(len(country_list)):
        if i == len(country_list) - 1:
            print(country_list[i][0])
        else:
            print(country_list[i][0], end=", ")


def add_country(data_list, country_list, j):
    country_list.append([])
    for k in range(len(data_list[j])):
        if k > 1:
            try:
                country_list[len(country_list) - 1].append(float(data_list[j][k]))
            except:
                print("Error with the file")
                exit(84)
        else:
            country_list[len(country_list) - 1].append(data_list[j][k])


def get_country(argv, data_list):
    country_list = []
    for i in range(1, len(argv)):
        find = False
        for j in range(len(data_list)):
            if argv[i] == data_list[j][1]:
                add_country(data_list, country_list, j)
                find = True
        if not find:
            print("Country not found")
            exit(84)
    print_country(country_list)
    return country_list


def get_fusionned_country(country_list):
    fusionned_country = []
    for i in range(2, len(country_list[0])):
        fusionned_country.append(country_list[0][i])
        for j in range(1, len(country_list)):
            fusionned_country[i - 2] += country_list[j][i]
    return fusionned_country


def get_means(list):
    return sum(list) / len(list)


def get_deviation(list, mean):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] - mean)
    return new_list
