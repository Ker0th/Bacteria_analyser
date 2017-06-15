from dataLoad import *
from Menu import *
import numpy as np
#data = dataLoad('test.txt')
#dataorigin = dataLoad('test.txt')
#c = np.zeros(len(data), dtype=bool)
def filterGrowth(gmin, gmax, data, c):
    '''

    :param gmin: a float
    :param gmax: a float
    :param data: An N x 3 matrix with columns Temperature, Growth rate, and Bacteria.
    :param c: Boolean array of False with the length of data
    :return: An N x 3 matrix with columns Temperature, Growth rate, and Bacteria.
    '''
    # creates the growth rate filter
    for i in range(len(data)):
        c[i] = (gmin <= data[i, 1] <= gmax)
    data = data[c]

    return data
def filterBac(bacTypes, data):
    '''

    :param bacTypes: Boolean of True with the length 4
    :param data: An N x 3 matrix with columns Temperature, Growth rate, and Bacteria.
    :return: a Modified boolean based on the users selection
    '''
    Bacterium = np.array(['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta', 'Reset selection', 'Back to parent menu'])
    while True:
        bactype = displayMenu(Bacterium)
        if bactype == 1:
            bacTypes[0] = False
            print('\nSalmonella enterica have been filtered away\n')
        elif bactype == 2:
            bacTypes[1] = False
            print('\nBacillus cereus have been filtered away\n')
        elif bactype == 3:
            bacTypes[2] = False
            print('\nListeria have been filtered away\n')
        elif bactype == 4:
            bacTypes[3] = False
            print('\nBrochothrix thermosphacta have been filtered away\n')
        elif bactype == 5:
            bacTypes = np.ones(4, dtype = bool)
            print('\nYour bacteria filter have been reset\n')
        elif bactype == 6:
            #print(bacTypes)
            print()
            break


    return bacTypes
#print(filter(0.5,0.8, data,np.zeros(len(data), dtype=bool)))
#data = filter(0.5,0.8, data, np.zeros(len(data), dtype=bool))
#print(len(data))
#print(len(dataorigin))
