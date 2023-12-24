# Напишите программу для печати всех уникальных значений в словаре.

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}] #это СПИСОК словарей

unique_values = set()

for dictionaries in list_1:
    for value in dictionaries.values():
        unique_values.add(value)

print(unique_values)