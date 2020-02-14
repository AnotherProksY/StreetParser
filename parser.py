"""Script for mapping streets and their districts."""
from sys import argv

DISTRICT_FILES = {
    "ЦАО": "CAO.txt",
    "САО": "SAO.txt",
    "СВАО": "SVAO.txt",
    "ВАО": "VAO.txt",
    "ЮВАО": "UVAO.txt",
    "ЮАО": "UAO.txt",
    "ЮЗАО": "UZAO.txt",
    "ЗАО": "ZAO.txt",
    "СЗАО": "SZAO.txt",
    "ЗЕЛАО": "ZELAO.txt"
}

STREET_LIST_FILE = f'{argv[1]}'


districts_count = {
    "ЦАО": 0,
    "САО": 0,
    "СВАО": 0,
    "ВАО": 0,
    "ЮВАО": 0,
    "ЮАО": 0,
    "ЮЗАО": 0,
    "ЗАО": 0,
    "СЗАО": 0,
    "ЗЕЛАО": 0
}


def read(filename):
    """Open file and read each line."""
    with open(filename, 'r') as f:
        document = f.readlines()
        return document


def street_parser(style="Raw"):
    """
    1. Iterate through DISTRICT_FILES dictionary.

       * Obtain "code : filename"
       * Assign return value from read() -> (list of file lines)

    2. Iterate through streets file.

       * reassign value to street variable -> (list of [street_name, count])

    3. Iterate through district_name -> (each line of DISTRICT_FILES.filename).

       * if line contains streets.street.name,
            then append street.count value to districts_count dictionary
    """
    streets = read(STREET_LIST_FILE)

    for code, filename in DISTRICT_FILES.items():
        district_name = read(filename)

        for street in streets:
            street = street.split(',')

            for line in district_name:
                if street[0] in line:
                    districts_count[code] += int(street[1])

    # After iterating and parsing, print dictionary values
    if style.lower() == "raw":
        print(districts_count)

    elif style.lower() == "format":
        for code, count in districts_count.items():
            print(f'Название округа: {code} -> количество вызовов: {count}\n')


if __name__ == "__main__":
    street_parser(f'{argv[2]}')
