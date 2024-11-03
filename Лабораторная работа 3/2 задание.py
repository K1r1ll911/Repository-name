def find_common_participants(group1, group2, rasdelitel=','):
    participants1 = set(group1.split(rasdelitel))
    participants2 = set(group2.split(rasdelitel))
    peresech = sorted(participants1.intersection(participants2))

    return peresech

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

a = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники (по умолчанию):", a)

b = find_common_participants(participants_first_group, participants_second_group,
                                                     rasdelitel='|')
print("Общие участники (с запятой):", b)