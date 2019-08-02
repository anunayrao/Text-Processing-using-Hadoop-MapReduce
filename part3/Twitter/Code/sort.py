import sys, csv ,operator
#sys.argv[0] - input file - part-0000.csv
#sys.argv[1] -output file
data = csv.reader(open(sys.argv[1]),delimiter=',')
sortedlist = sorted(data, key=lambda x: int(operator.itemgetter(1)(x)),reverse=True)    # 0 specifies according to first column we want to sort
#now write the sorte result into new CSV file
with open(sys.argv[2], "wb") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)