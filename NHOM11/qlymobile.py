import csv
def read_csv(ds_mobile):
    f = open(ds_mobile)
    for row in csv.reader(f):
        print(row)
        f.close()
