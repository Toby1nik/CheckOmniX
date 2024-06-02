import pandas as pd


def process_omnix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        address_percentages_omnix = {}

        header_skipped = False

        for line in lines:
            if not header_skipped:
                header_skipped = True
                continue

            address, percentage = line.strip().split(',')
            address_percentages_omnix[address.lower()] = float(percentage)

    return address_percentages_omnix


def process_clusters(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        address_percentages_clusters = {}

        header_skipped = False

        for line in lines:
            if not header_skipped:
                header_skipped = True
                continue

            address, percentage_with_percent = line.strip().split(',')
            percentage = float(percentage_with_percent.rstrip('%'))
            address_percentages_clusters[address.lower()] = percentage

    return address_percentages_clusters


def process_tavaera(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        address_percentages_tavaera = {}

        header_skipped = False

        for line in lines:
            if not header_skipped:
                header_skipped = True
                continue

            address, percentage = line.strip().split(',')
            address_percentages_tavaera[address.lower()] = float(percentage)

    return address_percentages_tavaera


def process_polyhedra(file_name):
    df_polyhedra = pd.read_excel(file_name)

    matching_addresses_polyhedra = []
    matching_percentages_polyhedra = []

    for address in df_polyhedra['address']:
        if address in wallet_addresses:
            matching_addresses_polyhedra.append(address)
            matching_percentages_polyhedra.append(df_polyhedra.loc[df_polyhedra['address'] == address, 'percentage'].iloc[0])

    total_percentage_polyhedra = sum(matching_percentages_polyhedra)

    return total_percentage_polyhedra, matching_addresses_polyhedra


def write_to_file(file_name, eligible_addresses):
    with open(file_name, 'w') as file:
        for address in eligible_addresses:
            file.write(address + '\n')


# Загрузка списка кошельков
# Загрузка списка кошельков
with open('wallets.txt', 'r') as file:
    lines = file.readlines()
    wallet_addresses = [line.strip().lower() for line in lines]

# Обработка файлов
address_percentages_omnix = process_omnix('OmniX.txt')
eligible_addresses_omnix = [address for address in wallet_addresses if address in address_percentages_omnix]
total_percentage_omnix = sum(address_percentages_omnix[address] for address in eligible_addresses_omnix)
write_to_file('eligible_omnix.txt', eligible_addresses_omnix)
print(f"Общий процент для OmniX: {total_percentage_omnix}% | Кол-во eligible кошельков: {len(eligible_addresses_omnix)}")

address_percentages_clusters = process_clusters('clusters.txt')
eligible_addresses_clusters = [address for address in wallet_addresses if address in address_percentages_clusters]
total_percentage_clusters = sum(address_percentages_clusters[address] for address in eligible_addresses_clusters)
write_to_file('eligible_cluster.txt', eligible_addresses_clusters)
print(f"Общий процент для Clusters: {total_percentage_clusters}% | Кол-во eligible кошельков: {len(eligible_addresses_clusters)}")

address_percentages_tavaera = process_tavaera('tevaera.txt')
eligible_addresses_tavaera = [address for address in wallet_addresses if address in address_percentages_tavaera]
total_percentage_tavaera = sum(address_percentages_tavaera[address] for address in eligible_addresses_tavaera)
write_to_file('eligible_tavaera.txt', eligible_addresses_tavaera)
print(f"Общий процент для Tavaera: {total_percentage_tavaera}% | Кол-во eligible кошельков: {len(eligible_addresses_tavaera)}")

print()
print('Обработка полихедры, софт не завис....')
print()


total_percentage_polyhedra, matching_addresses_polyhedra = process_polyhedra("polyhedra.xlsx")
write_to_file('eligible_polyhedra.txt', matching_addresses_polyhedra)
print(f"Общий процент для Polyhedra: {total_percentage_polyhedra:.8f}% | Кол-во eligible кошельков: {len(matching_addresses_polyhedra)}")
