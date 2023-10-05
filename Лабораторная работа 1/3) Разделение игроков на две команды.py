list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


middle = int(len(list_players) / 2)
first_team = list_players[0:middle]
second_team = list_players[middle::]
print(first_team, second_team, sep='\n')
#sep= еще не изучался в курсе, но я решила использовать его как один
#из способов не прописывать два принта
