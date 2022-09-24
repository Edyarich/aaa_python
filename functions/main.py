""" Parse csv file """
import argparse as ap
import sys
import csv
from typing import List, Tuple, Set, Dict, Any, Type, Optional


def read_csv(filename: str, **csv_options) -> List[List[str]]:
    """
    Read csv file
    :param filename: str
        Location of the csv file for reading data
    :param csv_options: optional
        Positional arguments passed to `csv.reader` object
    :return data_read: List[List[str]]
        Table, represented by list of lists of strings
    """
    with open(filename, 'r', encoding='utf-8') as fd:
        reader = csv.reader(fd, **csv_options)
        data_read = [row for row in reader]

    return data_read


def write_csv(filename: str, data: List[List[Any]], **csv_options) -> None:
    """
    Write table into csv file
    :param filename: str
        Location of the csv file for writing data
    :param data: List[List[Any]]
        Table, which will be saved in a file
    :param csv_options: optional
        Positional arguments passed to `csv.writer` object
    :return: None
    """
    with open(filename, 'a', encoding='utf-8') as fd:
        writer = csv.writer(fd, **csv_options)
        writer.writerows(data)


def split_df(df: List[List[str]]) -> Tuple[Dict[str, int], List[List[str]]]:
    """
    Split dataframe into header and body parts
    :param df: List[List[str]]
        Dataframe which contains a header and a body
    :return header: Dict[str, int]
        The dictionary with keys equal to `range(len(titles))` and values equal
        to the titles of df columns
    :return body: List[List[str]]
        Data extracted from df
    """
    header = dict(zip(df[0], range(len(df[0]))))
    body = df[1:]

    return header, body


def convert_types(df: List[List[str]], type_arr: Tuple[Type]) -> None:
    """
    Transform types of df columns INPLACE
    :param df: List[List[str]]
        Dataframe, whose all elements have type `str`
    :param type_arr: Tuple[type]
        Desired types of df columns
    :return: None
    """
    for df_row in df:
        for i in range(len(df_row)):
            df_row[i] = type_arr[i](df_row[i])


def get_department_structure(df: List[List[Any]],
                             header: Dict[str, int]) -> Dict[str, Set[str]]:
    """
    Extract divisions of departments from df
    :param df: List[List[Any]]
        Dataframe which contains information about departments structure
    :param header: Dict[str, int]
        Dataframe header which has fields 'Департамент' and 'Отдел'
    :return departments_and_teams: Dict[str, Set[str]]
        The dictionary with keys equal to department names and values equal
        to set of teams included in certain department
    """
    departments_and_teams = {}
    dep_ind = header['Департамент']
    team_ind = header['Отдел']

    for df_row in df:
        department = df_row[dep_ind]
        team = df_row[team_ind]

        if departments_and_teams.get(department) is None:
            departments_and_teams[department] = set()

        if team not in departments_and_teams[department]:
            departments_and_teams[department].add(team)

    return departments_and_teams


def print_department_structure(dep_structure: Dict[str, Set[str]],
                               filename: str) -> None:
    """
    Print department structure
    :param dep_structure: Dict[str, Set[str]
        The dictionary with keys equal to department names and values equal
        to set of teams included in certain department
    :param filename: Optional[str]
        Output file
    :return: None
    """
    fd = sys.stdout if filename == sys.stdout.name \
        else open(filename, 'a', encoding='utf-8')

    for department, teams in dep_structure.items():
        print(department, end=': ', file=fd)

        for i, team in enumerate(teams):
            if i == 0:
                print(team, file=fd)
            else:
                print(' ' * (len(department) + 1), team, file=fd)

    if fd != sys.stdout:
        fd.close()


def get_department_report(df: List[List[Any]],
                          header: Dict[str, int]) -> Dict[str, Dict[str, int]]:
    """
    Extract information about departments, which includes:
    staff size, min-max salary, average salary
    :param df: List[List[Any]]
        Dataframe which contains info about staff salaries
    :param header: Dict[str, int]
        Dataframe header which has fields 'Департамент' and 'Оклад'
    :return departments_and_info: Dict[str, Dict[str, int]]
        The dictionary with the following structure:
            {'department_name': {'count': int,
                                 'min': int,
                                 'max': int,
                                 'avg': float},
             ... }
    """
    departments_and_info = {}
    dep_ind = header['Департамент']
    salary_ind = header['Оклад']
    def_info = {'count': 0,
                'min': float('inf'),
                'max': float('-inf'),
                'avg': 0}

    for df_row in df:
        department = df_row[dep_ind]
        salary = df_row[salary_ind]

        if departments_and_info.get(department) is None:
            departments_and_info[department] = def_info.copy()

        departments_and_info[department]['count'] += 1
        departments_and_info[department]['avg'] += salary
        departments_and_info[department]['min'] = \
            min(salary, departments_and_info[department]['min'])
        departments_and_info[department]['max'] = \
            max(salary, departments_and_info[department]['max'])

    for department, info in departments_and_info.items():
        dep_size = info['count']
        info['avg'] /= dep_size

    return departments_and_info


def print_department_report(report: Dict[str, Dict[str, int]],
                            filename: str) -> None:
    """
    Print department report
    :param report: Dict[str, int]
        The dictionary with the following structure:
            {'department_name': {'count': int,
                                 'min': int,
                                 'max': int,
                                 'avg': float},
             ... }
    :param filename: str
        Output file or None (then filename == sys.stdout)
    :return: None
    """
    if len(report) == 0:
        return

    fd = sys.stdout if filename == sys.stdout.name \
        else open(filename, 'a', encoding='utf-8')

    header = list(report.values())[0].keys()
    header_format_str = '{:<32} {:<8} {:<16} {:<16} {:<16}'
    format_str = '{:<32} {:<8} {:<16} {:<16} {:.1f}'

    print(header_format_str.format('Department', *header), file=fd)
    for dep, info in report.items():
        info = info.values()
        print(format_str.format(dep, *info), file=fd)

    if fd != sys.stdout:
        fd.close()


def save_report(report: Dict[str, Dict[str, int]],
                filename: str, **csv_options) -> None:
    """
    Save department report into a file
    :param report: Dict[str, Dict[str, int]]
        The dictionary with the following structure:
            {'department_name': {'count': int,
                                 'min': int,
                                 'max': int,
                                 'avg': float},
             ... }
    :param filename: str
        Path to file
    :param csv_options: optional
        Positional arguments passed to `write_csv` function
    :return: None
    """
    if len(report) == 0:
        return

    header = list(report.values())[0].keys()
    data_to_save = [list(header)]

    for dep, info in report.items():
        df_row = [dep] + list(map(str, info.values()))
        data_to_save.append(df_row)

    write_csv(filename, data_to_save, **csv_options)


def key_func(args: ap.Namespace) -> None:
    """
    Implement high-level logic and do certain task depending on input
    :param args: argparse.Namespace
        Arguments passed to the parser
    :return: None
    """
    if args.command_num in (1, 2, 3):
        df = read_csv(args.csv_file.name, delimiter=args.delimiter)
        header, df = split_df(df)

        if args.command_num == 1:
            dep_structure = get_department_structure(df, header)
            print_department_structure(dep_structure, args.output.name)

        elif args.command_num in (2, 3):
            type_arr = [str] * len(header)
            for i in args.numeric_columns:
                type_arr[i] = float

            convert_types(df, type_arr)
            dep_report = get_department_report(df, header)
            out_filename = sys.stdout.name if args.command_num == 2 \
                else args.output.name
            print_department_report(dep_report, out_filename)

    else:
        print('Wrong command_num. See --help for details')


def get_parser() -> ap.ArgumentParser:
    """
    Build parser for the task
    :return parser: argparse.ArgumentParser
    """
    HELP_STR = 'Выберите действие, введя соответсвующее число: ' + \
               '1 - Вывести в понятном виде иерархию команд, ' + \
               'т.е. департамент и все команды, которые входят в него\n' + \
               '2 - Вывести сводный отчёт по департаментам: ' + \
               'название, численность, "вилка" зарплат в виде мин – макс, ' + \
               'среднюю зарплату\n' + \
               '3 - Сохранить сводный отчёт из предыдущего пункта в виде csv-файла'
    parser = ap.ArgumentParser(description=HELP_STR)
    parser.add_argument('command_num', type=int,
                        help='Номер команды')
    parser.add_argument('csv_file',
                        type=ap.FileType('rt'),
                        help='Csv файл с данными для обработки')
    parser.add_argument('--output',
                        type=ap.FileType('wt'),
                        default=sys.stdout,
                        help='Файл для вывода данных. ' + \
                             'По умолчанию осуществляется через консоль')
    parser.add_argument('--delimiter',
                        type=str,
                        default=';',
                        help='Разделитель, использующийся в csv файле')
    parser.add_argument('--numeric_columns',
                        type=int,
                        nargs='*',
                        default=[4, 5],
                        help='Номера столбцов с численными данными, ' + \
                             'начиная с нуля')
    parser.set_defaults(func=key_func)

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)
