import numpy as np
import pandas as pd
def dataLoad(filename):
    '''
    This function loads the users data and remove unuseble datalines, while informing the user about the issue
    :param filename: A string containing the filename of a data file
    :return: An N x 3 matrix
    '''
    Import = np.array(pd.read_csv(filename, sep=' ', header=None))
    #Finding out if a whole line is valid
    a = np.zeros(len(Import),dtype = bool)
    #Finding what value is invalid
    b = np.zeros(((len(Import),3)), dtype = bool)
    # Assigning True values to the data that can be used
    for i in range(len(Import)):
        b[i,0] = (10 < Import[i, 0] < 60)
        b[i,1] = ( Import[i, 1] > 0 )
        b[i,2] = (1 <= Import[i, 2] <= 4)
        a[i] = (10 < Import[i, 0] < 60) and ( Import[i, 1] > 0 ) and (1 <= Import[i, 2] <= 4)
    dataorigin = Import[a]
    #finding on what lines a given value is out of the given range
    print()
    for i in range(len(b)):
        if ((b[i,0] == False) and (b[i,1] == False) and (b[i,2] == False)):
            print('line {0} is invalid because all values are out of range'.format(i+1))
        elif ((b[i, 0] == False) and (b[i, 1] == False)):
            print('line {0} is invalid because the growth rate and temperature is out of range'.format(i + 1))
        elif ((b[i, 2] == False) and (b[i, 1] == False)):
            print('line {0} is invalid because the growth rate is out of range and Bacteria is not known'.format(i + 1))
        elif ((b[i,0] == False) and b[i,2] == False):
            print('Line {0} is invalid because the temperature is out of range and the bacteria is not known')
        elif b[i,0] == False:
            print('line {0} is invalid because the temperature is not in range'.format(i+1))
        elif b[i,1] == False:
            print('line {0} is invalid because the growth rate is not in range'.format(i + 1))
        elif b[i,2] == False:
            print('line {0} is invalid because the Bacteria is not known'.format(i + 1))
    print()


    return dataorigin