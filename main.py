import pandas as pd

# Открываем файл с процентами для каждого адреса (OmniX)
with open('OmniX.txt', 'r') as file:
    lines = file.readlines()
    address_percentages_omnix = {}

    # Пропускаем первую строку с заголовком
    header_skipped = False

    for line in lines:
        if not header_skipped:
            header_skipped = True
            continue

        address, percentage = line.strip().split(',')
        address_percentages_omnix[address.lower()] = float(percentage)


# Открываем файл с адресами для сравнения
with open('wallets.txt', 'r') as file:
    lines = file.readlines()

# Преобразуем список строк в список адресов, приводя их к нижнему регистру
wallet_addresses = [line.strip().lower() for line in lines]

# Проверяем, какие адреса из wallets.txt есть в address_percentages_omnix
total_percentage_omnix = 0
eligible_addresses_omnix = []

for address in wallet_addresses:
    if address in address_percentages_omnix:
        total_percentage_omnix += address_percentages_omnix[address]
        eligible_addresses_omnix.append(address)

# Записываем элегибл адреса в файл eligible_omnix.txt
with open('eligible_omnix.txt', 'w') as file:
    for address in eligible_addresses_omnix:
        file.write(address + '\n')

# Выводим результаты для OmniX
print(f"Общий процент для OmniX: {total_percentage_omnix}% | Кол-во eligible кошельков: {len(eligible_addresses_omnix)}")
print("Элегибл адреса OmniX записаны в файл eligible_omnix.txt")

print('')
print(f'НАХЕР ОПТИМИЗАЦИЮ ПАДАЖДИ ПОКА-что...... ДУМАЕМ.gif')
print('')

# Открываем файл с процентами для каждого адреса (Polyhedra)
df_polyhedra = pd.read_excel("polyhedra.xlsx")

# Создаем пустой список для сохранения адресов и процентов совпадающих адресов
matching_addresses_polyhedra = []
matching_percentages_polyhedra = []

# Проверяем каждый адрес из файла polyhedra.xlsx
for address in df_polyhedra['address']:
    if address in wallet_addresses:
        # Если адрес найден в списке адресов, сохраняем адрес и процент
        matching_addresses_polyhedra.append(address)
        matching_percentages_polyhedra.append(df_polyhedra.loc[df_polyhedra['address'] == address, 'percentage'].iloc[0])

# Считаем общий процент для Polyhedra
total_percentage_polyhedra = sum(matching_percentages_polyhedra)

# Выводим результаты для Polyhedra
print(f"Общий процент для Polyhedra: {total_percentage_polyhedra:.8f}% | Кол-во eligible кошельков: {len(matching_addresses_polyhedra)}")
print("Элегибл адреса Polyhedra записаны в файл eligible_polyhedra.txt")

# Сохраняем совпавшие адреса для Polyhedra в файл eligible_polyhedra.txt
with open('eligible_polyhedra.txt', 'w') as file:
    for address in matching_addresses_polyhedra:
        file.write(address + '\n')
