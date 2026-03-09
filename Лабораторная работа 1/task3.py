list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 #индекс, относительно которого будут разделены команды

first_team = list_players[:middle_index] #разделение игроков на первую команду
second_team = list_players[middle_index:] #разделение игроков на вторую команду

print(first_team)
print(second_team)
