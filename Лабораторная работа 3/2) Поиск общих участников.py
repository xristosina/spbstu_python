# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, separator=','):
    first_set = set(first_string.split(separator))
    second_set = set(second_string.split(separator))
    common_participants = list(first_set.intersection(second_set))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_third_group = "Иванов,Петров,Сидоров"
participants_forth_group = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_third_group, participants_forth_group))
