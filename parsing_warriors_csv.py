import csv
from random import randint

WARRIORS = []


class CSVFile:
    READ = 'r'
    DELIMITER = ','

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, self.READ) as file:
            reader = csv.DictReader(file, delimiter=self.DELIMITER)
            for line in reader:
                warrior = {
                    'name': line['name'],
                    'power': int(line['power']),
                    'hp': int(line['hp'])
                }
                WARRIORS.append(warrior)
            file.close()


file = CSVFile('warriors_table.csv')
file.read()
