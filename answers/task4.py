def read_csv(filename):
    import csv
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            print(row)
            break
    csvFile.close()


read_csv('sample.csv')
