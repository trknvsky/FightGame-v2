import csv
from random import randint


WARRIORS = [
    {
        'name': 'strength man',
        'hp': 100,
        'power': 11
    }, {
        'name': 'agility man',
        'hp': 75,
        'power': 15
    }, {
        'name': 'intelligence man',
        'hp': 85,
        'power': 14
    }
]


class CSVFile:
    WRITE = 'a'
    DELIMITER = ','
    HEADERS = ['name', 'power', 'hp']

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, self.WRITE, newline='') as file:
            writer = csv.DictWriter(file, delimiter=self.DELIMITER, fieldnames=self.HEADERS)
            writer.writeheader()
            writer.writerows(data)
            file.close()


file = CSVFile('warriors_table.csv')
file.write(WARRIORS)
