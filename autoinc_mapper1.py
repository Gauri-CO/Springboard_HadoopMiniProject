import sys

for line in sys.stdin:
    line.strip()
    incident_id, incident_type, vin_number, make, model, year, incident_year, description = line.split(",")
    results = [vin_number, incident_type, make, year]
    print('%s\t%s\t%s\t%s' % (vin_number, incident_type, make, year))












