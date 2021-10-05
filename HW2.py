import csv
from collections import defaultdict


def return_hierarchy(filename: str) -> dict:
    """
    This function returns the hierarchy of the company from a given database in csv-file
    """

    dict_deps = defaultdict(set)

    with open(filename) as file:
        data = csv.DictReader(file, delimiter=';')
        for row in data:
            department = row['Департамент']
            team = row['Отдел']
            dict_deps[department].add(team)

    return dict_deps


def return_info(filename: str) -> (dict, list):
    """
    This function returns the info about number of workers and salaries
    """

    dict_info = defaultdict(lambda: {'Зарплаты': [], 'Численность': 0})
    header = ['Департамент', 'Численность', 'Макс.зарплата', 'Мин.зарплата', 'Средняя зарплата']

    with open(filename) as file:
        data = csv.DictReader(file, delimiter=';')
        for row in data:
            department = row['Департамент']
            salary = float(row['Оклад'])
            dict_info[department]['Зарплаты'].append(salary)
            dict_info[department]['Численность'] += 1

    for dep in dict_info:
        dict_info[dep]['Мин.зарплата'] = min(dict_info[dep]['Зарплаты'])
        dict_info[dep]['Макс.зарплата'] = max(dict_info[dep]['Зарплаты'])
        dict_info[dep]['Средняя зарплата'] = round(sum(dict_info[dep]['Зарплаты']) / len(dict_info[dep]['Зарплаты']), 1)
        del dict_info[dep]['Зарплаты']

    return dict_info, header


def create_csv(input_filename: str, output_filename: str):
    """
    This function creates csv-file with info about department.
    """
    dict_info, header = return_info(input_filename)

    with open(output_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, delimiter=';')
        writer.writeheader()

        for department, info in dict_info.items():
            to_write = {'Департамент': department}
            to_write.update(info)
            writer.writerow(to_write)

    print('Файл находится в папке, откуда запустился код.')


def menu():
    print('\n',
          '1.Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него',
          '\n',
          '2.Вывести сводный отчёт по департаментам: название, численность,'
          ' "вилка" зарплат в виде мин – макс, среднюю зарплату',
          '\n',
          '3.Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. '
          'При этом необязательно вызывать сначала команду из п.2',
          '\n')

    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if option == '1':
        hierarchy = return_hierarchy('corp_summary_edm.csv')
        for department, teams in hierarchy.items():
            print(f'Департамент "{department}":')
            k = 1
            for team in teams:
                print(f'\t {k}.{team}')
                k += 1

    elif option == '2':
        dict_info, header = return_info('corp_summary_edm.csv')

        print("{:<12}| {:<12}| {:<15}| {:<15}| {:<10}".format(*header))
        print('-------------------------------------------------------------------------------')

        for department, info in dict_info.items():
            n, min_s, max_s, avg_s = info['Численность'], \
                                     info['Мин.зарплата'], \
                                     info['Макс.зарплата'], \
                                     info['Средняя зарплата']
            print("{:<12}| {:<12}| {:<15}| {:<15}| {:<10}".format(department, n, max_s, min_s, avg_s))

    elif option == '3':
        create_csv('corp_summary_edm.csv', 'summary_corp.csv')


if __name__ == '__main__':
    menu()
