import csv
def deduplicate():
    with open('./files/companies_out.csv', 'r') as csvfile, open('./files/companies_out_deduplicated.csv', 'a') as out_file:
        seen = set()
        companies = csv.reader(csvfile, delimiter=';', quotechar='"')

        for company in companies:
            if company[1] in seen:
                continue
            seen.add(company[1])
            out_file.write(company[0])
            out_file.write(";")
            out_file.write(company[1])
            out_file.write("\n")
