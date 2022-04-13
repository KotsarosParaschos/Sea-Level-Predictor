import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
   
    df = pd.read_csv('epa-sea-level.csv')  #reads data from file
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level']) # creates scatter plot
    
    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xa = np.arange(df['Year'].min(),2050,1)        # creates the first line of the best fit
    ya = xa*lineA.slope + lineA.intercept
    plt.plot(xa,ya)
    
    df_2000 = df[df['Year'] >= 2000]
    lineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    xb = np.arange(2000,2050,1)                  # creates the second line of the best fit
    yb = xb*lineB.slope + lineB.intercept
    plt.plot(xa,yb)
    
    
    plt.title('Rise in sea level')
    plt.xlabel('Year')    #title and labels
    plt.ylabel('Sea level')      

    plt.savefig('sea_level_plot.png')
    return plt.gca()   #saves the plot
