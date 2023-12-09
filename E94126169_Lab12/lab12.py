import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    data = []
    with open(filename) as file:
        file.seek(9)
        for line in file:
            year = map(float, line.split(", ")[1:])
            data.append(np.asarray(list(year)))
        
    return data

def Monly_temperature_figure1(data, ax):
    month = np.linspace(1,12,12)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature in Degree C")
    ax.set_title("Tainan Monthly Mean Temperature From 2013 To 2021")
    ax.set_xticks(month)
    

    for i, year_temperature in enumerate(data):
        ax.plot(month, year_temperature, label=2013+i)
    ax.legend(loc="lower center")
    
    

def the_average_temperature_each_month(data):
    months_average = np.linspace(0,0,12)
    for arr in data:
        months_average += arr
    
    months_average /= 9
    nine_years_mean = np.mean(months_average)
    return np.around(months_average, 2), np.around(nine_years_mean, 2)
      
def Monly_temperature_figure2(data, ax):
    month = np.linspace(1,12,12)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature in Degree C")
    ax.set_title("Tainan Monthly Mean Temperature From 2013 To 2021")
    ax.set_xticks(month)
    ax.set_ylim(16,32)

    months_average, total_average = the_average_temperature_each_month(data)

    ax.plot(month, months_average)
    ax.scatter(month, months_average, color="red")
    for i, label in enumerate(months_average):
        ax.text(month[i], months_average[i], label)
    
    ax.axhline(total_average, color="red", linestyle="--", label="Mean of 9 Years")
    ax.text(1,25,total_average)
    ax.legend()
    
    

    
def main():
    data = read_data(filename="Temperature.txt")
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(1,2, figsize=(15,6))
    Monly_temperature_figure1(data, ax[0])
    Monly_temperature_figure2(data, ax[1])
    fig.savefig("lab12_03.png")

main()