import csv

names = []
addresses = []

with open('ads.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        names.append(row[2])
        addresses.append(row[5])
set_names = (list(set(names)))
set_names.remove('author')
names_dict = {}
n = 1
for name in set_names:
    names_dict[name] = n
    n += 1


with open('name.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for num, name in names_dict.items():
        nam = [num, name]
        writer.writerow(nam)

set_addresses = (list(set(addresses)))
set_addresses.remove('address')
addresses_dict = {}
n = 1
for address in set_addresses:
    addresses_dict[address] = n
    n += 1


with open('address.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for num, address in addresses_dict.items():
        addr = [num, address]
        writer.writerow(addr)


with open('ads.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        id = row['Id']
        name = row['name']
        author = names_dict[row['author']]
        price = row['price']
        description = row['description']
        address = addresses_dict[row['address']]
        is_published = row['is_published']
        with open('new_ads.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(
                (
                    id,
                    name,
                    author,
                    price,
                    description,
                    address,
                    is_published
                )
            )


