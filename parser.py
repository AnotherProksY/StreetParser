# -*- coding: utf-8 -*-
"""Script for mapping streets and their districts."""

import sys
import json
import csv


class FileObject:
    """Get data from file."""

    def __init__(self, filename):
        """Specify filename to process."""
        self.filename = filename
        self.__load()

    def __load(self):
        """Load 'JSON/CSV' file."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            # Load JSON
            if self.filename.endswith('.json'):
                self.data = json.load(file)

            # Load CSV
            elif self.filename.endswith('.csv'):
                self.data = []

                # Assign reader object to temporiry variable
                temp = csv.reader(file)
                for row in temp:
                    self.data.append(row)

                # Get rid of 'CSV' header
                del self.data[0]


def street_parser(style="raw"):
    """Iterate through CSV file and compare to JSON.

    Args:
      style: String that defines 'print()' style.

    Returns:
      None.

    Styles preview:
    >>> street_parser()
    {'ЦАО': 197, 'САО': 38, 'СВАО': 37, 'ВАО': 11, ...}
    >>> street_parser(style="raw")
    {'ЦАО': 197, 'САО': 38, 'СВАО': 37, 'ВАО': 11, ...}
    >>> street_parser(style="format")
    Название округа: ЦАО -> количество улиц: 197
    Название округа: САО -> количество улиц: 38
    ...
    """
    # Iterate through STREETS CSV.
    #  * Get street 'name' and 'count' value
    #  * Get first 'letter' from street name
    for street, count in STREETS.data:
        f_letter = street[:1]

        # Iterate through DISTRICTS JSON.
        #  * Obtain districts 'code'
        #  * Get data from district 'code'
        for district in DISTRICTS.data:
            district_data = DISTRICTS.data[district]

            # If district contains streets with the same 'letter'.
            #  * True  -> check each street; write to 'districts_count'
            #  * False -> go to next district 'code'
            if district_data.get(f_letter):
                for dis_street in district_data[f_letter]:
                    if street in dis_street:
                        districts_count[district] += int(count)

    # After iterating and parsing, print dictionary values
    if style.lower() == "raw":
        print(districts_count)

    elif style.lower() == "format":
        for code, count in districts_count.items():
            print(f"Название округа: {code} -> количество улиц: {count}")


DISTRICTS = FileObject("dataset.json")

STREETS = FileObject(str(sys.argv[1]))


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
    "ЗЕЛАО": 0,
}


if __name__ == "__main__":
    street_parser(str(sys.argv[2]))
