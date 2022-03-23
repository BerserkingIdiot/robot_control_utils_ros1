import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import csv

with open("output/sample2.csv") as file: 
    csv_data = list(csv.reader(file, delimiter=','))

    # create a figure and axes
    fig = plt.figure(figsize=(12,5))
    ax1 = plt.subplot(1,1,1)   

    # set up the subplots as needed
    ax1.set_xlim(( 0, 180))            
    ax1.set_ylim((0, 30))
    ax1.set_xlabel('Laser')
    ax1.set_ylabel('Range')

    # create objects that will change in the animation. These are
    # initially empty, and will be given new values for each frame
    # in the animation.
    txt_title = ax1.set_title('')
    line1, = ax1.plot([], [], 'b', lw=2)     # ax.plot returns a list of 2D line objects
    #line2, = ax1.plot([], [], 'r', lw=2)

    def number_converter(n_string):
        if n_string == "nan":
            n = 30.0
        else:
            n = float(n_string)
        return n

    # animation function. This is called sequentially
    def drawframe(n):
        x = np.linspace(0, 178, 179)
        y1 = list(map(number_converter, csv_data[n+1][5:184]))
        #print("length: ", len(y1))
        #print(x)
        #print(n)
        #y2 = np.cos(2 * np.pi * (x - 0.01 * n))
        line1.set_data(x, y1)
        #line2.set_data(x, y2)
        txt_title.set_text('Frame = {0:4d}'.format(n))
        return line1,

    # blit=True re-draws only the parts that have changed.
    anim = animation.FuncAnimation(fig, drawframe, frames=len(csv_data)-1, interval=20, blit=True)

    plt.show()