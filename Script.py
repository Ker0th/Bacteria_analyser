from Data_statistic import *
from dataLoad import *
from Menu import *
from Filter import *
from PlotFunction import *

#Defining variables
reffbac = np.array([1,2,3,4])
bacTypes = np.ones(4, dtype = bool)
gmin = 0
gmax = 1
data = np.zeros(3)
#Defining our menu
menuItems = np.array([' Load data', ' Filter data', ' Display statistics', ' Generate plots', ' Quit'])
while True:
    choice = displayMenu(menuItems)
    try:
        if choice == 1:
            filename = str(input('Please enter a filename: '))
            dataorigin = data = dataLoad(filename)
    except FileNotFoundError:
        print('\nwrong file type\n')
    else:
        if choice == 2:
            if data.any() == 0:
                print("\nError: No data has been loaded\n")
            else:
                # run Filter function
                filtItems = np.array([' Growth rate filter', ' Bacteria filter', ' Reset filter',' Back to main menu\n'])
                print('\nPlease select a type of filter\n')
                #Resetting data
                data = dataorigin
                d = np.zeros(len(data))
                while True:
                    filt = displayMenu(filtItems)
                    if filt == 1:
                        while True:
                            try:
                                gmin = float(input('\nWrite the minimum value allowed for the bacteria growth rate: '))
                                gmax = float(input('\nWrite the maximum value allowed for the bacteria growth rate: '))
                                print()
                            except ValueError:
                                print('Error: that is not a number')
                            else:
                                if  not((0.0 <= gmin <= 1.0) and (gmin < gmax) and (0.0 <= gmax <= 1.0)):
                                    print('\nError: The values should be between 0 and 1 and the minimum value should be smaller than the maximum\n')
                                    continue
                                break
                        data = filterGrowth(gmin,gmax,data,np.zeros(len(data), dtype=bool))
                    if filt == 2:
                        bacTypes = filterBac(bacTypes, data)

                        #Finding user selected bacteria
                        bacteria = reffbac[bacTypes]
                        m_data = np.ma.masked_array(data)
                        m_data[:, 2] = np.ma.masked_where(~np.in1d(m_data[:, 2], bacteria), m_data[:, 2])
                        filter = ~m_data[:, 0].mask & ~m_data[:, 1].mask & ~m_data[:, 2].mask
                        data = data[filter,:]

                    #Resetting data
                    if filt == 3:
                        data = dataorigin

                    if filt == 4:
                        print('\nGoing to the main menu\n')
                        break
        elif choice == 3:
            if data.any() == 0:
                print('\nError: No data has been loaded\n')
            else:
                # run statistic function
                statItems = np.array([' Mean Temperature', ' Mean Growth rate', ' Std Temperature', ' Std Growth rate', ' Rows', ' Mean Cold Growth rate', ' Mean Hot Growth rate'])
                while True:
                    statis = displayMenu(statItems)
                    statistic = statItems[statis-1]
                    result = dataStatistics(data, statistic)
                    print()
                    print('The number of{0} is: '.format(statistic), result)
                    print()
                    break
        elif choice == 4:
            # run plot function
            if data.any() == 0:
                print('\nError: No data has been loaded\n')
            else:
                print('\nClose the plots to continue\n')
                dataPlot(data,gmin,gmax)
        elif choice == 5:
            #stop the program
            print('\nQuitting program')
            break

