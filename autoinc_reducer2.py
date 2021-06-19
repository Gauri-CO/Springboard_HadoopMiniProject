import sys

accidentrecord = {}

for line in sys.stdin:
    line = line.strip()

    line = line.split("\t")
    make = line[0]
    year = line[1]
    count = line[2]

    try:
        count = int(count)
    except ValueError:
        continue

    try:
        accidentrecord[(make, year)] = accidentrecord[(make, year)] + count

    except:
        accidentrecord[(make, year)] = count

for make, year in accidentrecord.keys():
    print('%s\t%s\t%s' % (make, year, accidentrecord[(make, year)]))
