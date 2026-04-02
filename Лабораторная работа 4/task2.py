import csv # Импортируем библиотеку
import json # Импортируем библиотеку

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None: # Задаем функцию
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file: # Cчитываем содержимое csv файла
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file: # Сериализовываю в файл с отступами равными 4
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
