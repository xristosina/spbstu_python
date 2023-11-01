import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение CSV файла и создание списка словарей
    with open(INPUT_FILENAME, mode='r', newline='') as csv_file:
        data = [row for row in csv.DictReader(csv_file)]

    # Сериализация данных в формат JSON с отступами
    with open(OUTPUT_FILENAME, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
