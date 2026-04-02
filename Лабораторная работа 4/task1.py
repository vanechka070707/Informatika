import json # Импортируем библиотеку

with open('input.json', 'r') as file: # Открываем файл
    data = json.load(file)

total = 0.0 # Вводим переменную для суммы

for item in data: # Проходим по каждому элементу в списке
    total = total + item['score'] * item['weight'] # Считаем сумму

result = round(total, 3) # Округляем результат до 3 знаков после запятой
print(result)
