import sys
# input comes from STDIN (standard input)

line1=[]
for line in sys.stdin:
# [derive mapper output key values]
    line = line.strip()

    # parse the input we got from mapper.py
    line1 = line.split('\t')
    if len(line1) > 1:
        make=line1[1]
        year=line1[2]

    print('%s\t%s\t%d' %(make,year,1))