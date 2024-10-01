import csv

# Загрузка строк из текстового файла "Input"
with open('Input.txt', 'r', encoding='utf-8') as input_file:
    input_lines = {line.strip() for line in input_file}

# Загрузка данных из CSV файла "All"
with open('All.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    all_data = {row[0].strip() for row in csv_reader}  # Предполагаем, что нужные данные в первом столбце

# Находим совпадения
eligible_matches = input_lines.intersection(all_data)

# Записываем совпадения в текстовый файл "Eligible"
with open('Eligible.txt', 'w', encoding='utf-8') as eligible_file:
    for match in eligible_matches:
        eligible_file.write(match + '\n')

print("Сопоставление завершено. Результаты записаны в 'Eligible.txt'.")