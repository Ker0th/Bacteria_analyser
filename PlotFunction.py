import numpy as np
import matplotlib.pyplot as plt



def dataPlot(data,gmin,gmax):
    '''

    :param data: An N x 3 matrix with columns Temperature, Growth rate, and Bacteria.
    :param gmin: A float
    :param gmax: A float
    :return: None
    '''
    #Defining starting values for number of bacteria before count.
    a=0
    b=0
    c=0
    d=0
    for i in range(len(data)):
        #Counting amount of each of the 4 bacteria
        if data[i,2]==1:
            a+=1
        elif data[i,2]==2:
            b+=1
        elif data[i,2]==3:
            c+=1
        elif data[i,2]==4:
            d+=1

    #Plotting amount of bacteria as a bar plot.
    y = np.array([a, b, c, d]) #
    x=np.arange(1,5)
    plt.figure(figsize=(20, 10))
    bar1=plt.bar(x[0],y[0],0.5,color='green')
    bar2=plt.bar(x[1],y[1],0.5,color='red')
    bar3=plt.bar(x[2],y[2],0.5,color='blue')
    bar4=plt.bar(x[3],y[3],0.5,color='y')
    plt.xlabel('Type of bacteria')
    plt.ylabel('Number of bacteria')
    plt.title('Number of bacteria')

    frame = plt.gca()
    frame.axes.get_xaxis().set_ticks([1,2,3,4])#fjerner talværdier fra x akse
    #frame.axes.get_yaxis().set_ticks([5,11,20,27])#fjerner talværdier fra y akse
    plt.text(0.75,25,'The filter applied for growth rate: \nThe minimum growth value applied is {0}\nThe maximum growth value applied is {1}'.format(gmin,gmax),bbox={'facecolor':'white','alpha':0.5})
    plt.legend((bar1,bar2,bar3,bar4), ("Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta"),bbox_to_anchor=(1,1))

    #new plot

    #Plotting Growth rate by temperature

    sorteddata = data[data[:, 0].argsort()] # Sorting the datafile by temperature, with corresponding growth rate and bacterium

    bacteria1 = sorteddata[sorteddata[:, 2] == 1]
    bacteria2 = sorteddata[sorteddata[:, 2] == 2]
    bacteria3 = sorteddata[sorteddata[:, 2] == 3]
    bacteria4 = sorteddata[sorteddata[:, 2] == 4]

    plt.figure(figsize=(20,10))

    p1=plt.plot(bacteria1[:,0],bacteria1[:,1],"-oy")
    p2=plt.plot(bacteria2[:,0],bacteria2[:,1],"-or")
    p3=plt.plot(bacteria3[:,0],bacteria3[:,1],"-og")
    p4=plt.plot(bacteria4[:,0],bacteria4[:,1],"-ob")
    plt.xlabel('Temperature')
    plt.ylabel('Growth rate')
    plt.title('Growth rate by temperature')
    plt.text(10,0.85,'The filter applied for growth rate: \nThe minimum growth value applied is {0}\nThe maximum growth value applied is {1}'.format(gmin,gmax),bbox={'facecolor':'white','alpha':0.5})
    plt.legend(["Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta"],loc='upper right',bbox_to_anchor=(1,1))

    plt.show()

#print(dataPlot(data))




