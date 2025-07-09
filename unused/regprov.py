import csv

# Load province to region mapping from province-data.csv
province_to_region = {}
with open('province-data.csv', newline='', encoding='utf-8') as ref:
    reader = csv.DictReader(ref)
    for row in reader:
        # Normalize province names (remove spaces, lowercase)
        key = row['province'].replace(' ', '').lower()
        province_to_region[key] = row['region']

# Process the target CSV and add region
with open('province_and_dates_no_spaces.csv', newline='', encoding='utf-8') as infile, \
     open('province_and_dates_with_region.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    # Insert 'Region' as the second column
    writer.writerow([header[0], 'Region'] + header[1:])
    for row in reader:
        province = row[0]
        key = province.replace(' ', '').lower()
        region = province_to_region.get(key, 'UNKNOWN')
        writer.writerow([province, region] + row[1:])