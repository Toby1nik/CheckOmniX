# Открываем файл с процентами для каждого адреса
with open('OmniX.txt', 'r') as file:
    lines = file.readlines()
    address_percentages = {}

    # Пропускаем первую строку с заголовком
    header_skipped = False

    for line in lines:
        if not header_skipped:
            header_skipped = True
            continue

        address, percentage = line.strip().split(',')
        address_percentages[address.lower()] = float(percentage)


# Открываем файл с адресами для сравнения
with open('wallets.txt', 'r') as file:
    lines = file.readlines()

# Преобразуем список строк в список адресов, приводя их к нижнему регистру
wallet_addresses = [line.strip().lower() for line in lines]

# Проверяем, какие адреса из wallets.txt есть в address_percentages
total_percentage = 0
eligible_addresses = []

for address in wallet_addresses:
    if address in address_percentages:
        total_percentage += address_percentages[address]
        eligible_addresses.append(address)

# Записываем элегибл адреса в файл eligible.txt
with open('eligible.txt', 'w') as file:
    for address in eligible_addresses:
        file.write(address + '\n')

# Выводим результаты
print(f"Общий процент: {total_percentage}% | Кол-во eligible кошелей: {len(eligible_addresses)}")
print("Элегибл адреса записаны в файл eligible.txt")
