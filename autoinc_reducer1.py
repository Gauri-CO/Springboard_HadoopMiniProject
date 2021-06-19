import sys

current_vin = None
vin = None
make = None
year = None
accident = False


def reset():
    current_vin = None
    vin = None
    make = None
    year = None
    accident = False


def flush():
    print('%s\t%s\t%s' % (current_vin, make, year))


for line in sys.stdin:

    line.strip()
    line = line.split('\t')
    vin = line[0]
    incident_type = line[1]

    if current_vin == vin:
        if incident_type == "I":
            make = line[2]
            year = line[3]

    if current_vin != vin:
        if current_vin is not None:
            flush()
        reset()

    if incident_type == "I":
        make = line[2]
        year = line[3]

    current_vin = vin


flush()