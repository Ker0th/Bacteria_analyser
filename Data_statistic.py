import numpy as np
def dataStatistics(data, statistic):
    '''


    :param data: An N x 3 matrix with columns Temperature, Growth rate, and Bacteria
    :param statistic: A string specifying the statistic that should be calculated
    :return: A scalar containing the calculated statistic
    '''

    # Taking the mean of the first column
    if statistic == " Mean Temperature":
        result = np.mean(data[:,0])

    # Taking the mean of the second column
    if statistic == " Mean Growth rate":
        result = np.mean(data[:,1])

    # Finding the standard deviation of the first column
    if statistic == " Std Temperature":
        result = np.std(data[:,0])

    # Finding the standard deviation of the second column
    if statistic == " Std Growth rate":
        result = np.std(data[:,1])

    # Total number of rows
    if statistic == " Rows":
        result = len(data)
        #result = len(data[:, 1]

    if statistic == " Mean Cold Growth rate":

        # Create a new array of all the data where the temperature < 20
        Sort = data[np.array(data[:, 0] < 20)]
        if np.size(Sort) == 0:
            print("There are no such data")
            result = "N/A"
        elif np.size(Sort) > 0:
            result = np.mean(Sort[:, 1])


    if statistic == " Mean Hot Growth rate":

        # Creates a new array of all the date where the temperature > 50
        Sort = data[np.array(data[:, 0] > 50)]
        if np.size(Sort) == 0:
            print("There are no such data")
            result = "N/A"
        elif np.size(Sort) > 0:
            result = np.mean(Sort[:, 1])


    return result
