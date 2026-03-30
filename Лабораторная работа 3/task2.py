def find_common_participants(first_group, second_group, separator=','): #Пишем функцию для поиска общих участников
    first_list = first_group.split(separator) #Разбиваем первую строку на список имен
    second_list = second_group.split(separator) #Разбиваем вторую строку на список имен
    return sorted(set(first_list) & set(second_list)) #Возвращаем сортированный результат, преобразовав списки в множества

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants("Иванов,Петров", "Петров,Сидоров"))
