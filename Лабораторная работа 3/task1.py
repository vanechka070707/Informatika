def find_index_item(items_list, item): # Создаю функцию для поиска индекса первого вхождения элемента в списке товаров.
    if item in items_list: # Условие входа элемента в список
        return items_list.index(item) # Возвращаю индекс элемента из списка
    else:
        return None # Возвращаю None при не нахождении элемента в списке

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
