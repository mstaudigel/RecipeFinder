import csv


with open('recipes.csv') as inputFile, open('recipes_new.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(inputFile):
        if any(field.strip() for field in row):
            writer.writerow(row)
    inputFile.close()
    output.close()
