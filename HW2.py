import csv


def return_hierarchy(filename: str) -> dict:
    """
    This function returns the hierarchy of the company from a given database in csv-file
    """

    dict_deps = {}

    with open(filename) as file:
        data = csv.DictReader(file, delimiter=';')
        for row in data:
            department = row['Департамент']
            value = row['Отдел']
            if department in dict_deps:
                if value in dict_deps[department]:
                    pass
                else:
                    dict_deps[department].append(value)
            else:
                dict_deps[department] = []

    return dict_deps


def return_info(filename: str) -> (dict, list):
    """
    This function returns the info about number of workers and salaries
    """

    dict_info = {}
    header = ['Департамент', 'Численность', 'Макс. зарплата', 'Мин. зарплата', 'Средняя зарплата']

    with open(filename) as file:
        data = csv.DictReader(file, delimiter=';')
        for row in data:
            department = row['Департамент']
            salary = float(row['Оклад'])
            if department in dict_info:
                dict_info[department]['Зарплаты'].append(salary)
                dict_info[department]['Численность'] += 1
            else:
                dict_info[department] = {'Зарплаты': [], 'Численность': 0}

    for i in dict_info:
        dict_info[i]['Мин.зарплата'] = min(dict_info[i]['Зарплаты'])
        dict_info[i]['Макс.зарплата'] = max(dict_info[i]['Зарплаты'])
        dict_info[i]['Средняя зарплата'] = round(sum(dict_info[i]['Зарплаты']) / len(dict_info[i]['Зарплаты']), 1)
        del dict_info[i]['Зарплаты']

    return dict_info, header


def create_csv(input_filename: str, output_filename: str):
    """
    This function creates csv-file with info about department.
    """
    header = ['Департамент', 'Численность', 'Макс. зарплата', 'Мин. зарплата', 'Средняя зарплата']

    dict_info = {}

    with open(input_filename) as file:
        data = csv.DictReader(file, delimiter=';')
        for row in data:
            department = row['Департамент']
            salary = float(row['Оклад'])
            if department in dict_info:
                dict_info[department]['Зарплаты'].append(salary)
                dict_info[department]['Численность'] += 1
            else:
                dict_info[department] = {'Зарплаты': [], 'Численность': 0}

    for i in dict_info:
        dict_info[i]['Мин.зарплата'] = min(dict_info[i]['Зарплаты'])
        dict_info[i]['Макс.зарплата'] = max(dict_info[i]['Зарплаты'])
        dict_info[i]['Средняя зарплата'] = round(sum(dict_info[i]['Зарплаты']) / len(dict_info[i]['Зарплаты']), 1)
        del dict_info[i]['Зарплаты']

    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for department, info in dict_info.items():
            writer.writerow([department, *list(info.values())])
    print('Файл находится в папке, откуда запустился код.')


print('\n',
      '1.Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него',
      '\n',
      '2.Вывести сводный отчёт по департаментам: название, численность,'
      ' "вилка" зарплат в виде мин – макс, среднюю зарплату',
      '\n',
      '3.Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. '
      'При этом необязательно вызывать сначала команду из п.2',
      '\n')


def menu():
    option = ''
    options = [1, 2, 3]
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = int(input())

    if option == 1:
        hierarchy = return_hierarchy('corp_summary_edm.csv')
        for i in hierarchy:
            print(f'Департамент "{i}":')
            k = 1
            for j in hierarchy[i]:
                print(f'\t {k}.{j}')
                k += 1

    elif option == 2:
        dict_info, header = return_info('corp_summary_edm.csv')

        print("{:<12}| {:<12}| {:<15}| {:<15}| {:<10}".format(*header))
        print('-------------------------------------------------------------------------------')

        for department, info in dict_info.items():
            n, min_s, max_s, avg_s = info.values()
            print("{:<12}| {:<12}| {:<15}| {:<15}| {:<10}".format(department, n, max_s, min_s, avg_s))

    elif option == 3:
        create_csv('corp_summary_edm.csv', 'summary_corp.csv')


if __name__ == '__main__':
    menu()
