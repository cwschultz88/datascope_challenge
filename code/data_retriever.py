import os
import csv

'''
contains method to get cta_data
'''

def get_cta_data():
    '''
    returns a list containing tuples of cta data
    '''
    path_to_datafile = os.path.join('data', 'cta_ridership.csv')
    datafile = open(path_to_datafile, 'rU')
    csv_reader = csv.reader(datafile)

    cta_data = []

    # read in data
    for dataline in csv_reader:
        # skip empty lines
        if not dataline:
            continue

        cta_data.append(tuple(data for data in dataline))

    datafile.close()
    return cta_data
