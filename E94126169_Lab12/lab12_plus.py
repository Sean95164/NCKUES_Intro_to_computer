import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def read_data(filename):
    data_x = []
    data_y = []
    with open(filename) as file:
        firstline = True
        for line in file:
            if(firstline):
                firstline = False
                continue
            y, x = map(float, line.split(" "))
            data_x.append(x)
            data_y.append(y)
    return np.asarray(data_x), np.asarray(data_y)

def oddExperiment_scatter(data, ax):
    x_ticks = np.arange(-10.0, 10.1, 2.5)
    ax.set_title("oddExperiment Data")
    ax.set_xticks(x_ticks)

    x, y = data
    
    line = ax.scatter(x, y, label="Data")
    return line

def find_linear_trend_line_equation(data):
    x, y = data
    coefficients = np.polyfit(x, y, 1)
    return np.poly1d(coefficients)

def fine_square_trend_line_equation(data):
    x, y = data
    coefficients = np.polyfit(x, y, 2)
    return np.poly1d(coefficients)

def trend_line_dg1(data, ax):
    x = np.linspace(-10.0, 10.0, 100)
    func = find_linear_trend_line_equation(data)
    y = func(x) 
    ax.plot(x, y, color="red")

def trend_line_dg2(data, ax):
    x = np.linspace(-10.0, 10.0, 100)
    func = fine_square_trend_line_equation(data)
    y = func(x)
    ax.plot(x, y, color="purple")

def LSE_and_RSquare(data, equation):
    x_p, y_p = data
    mean = np.mean(y_p)
    y_i = equation(x_p)
    diff_square = (y_i - y_p)**2
    LSE = np.mean(diff_square)
    RSquare = 1 - (np.sum(diff_square)/np.sum((y_p-mean)**2))
    return np.around(LSE, 5), np.around(RSquare, 5)

def calculate_and_set_legent(data, ax, line):
    LSE1, R2_1 = LSE_and_RSquare(data, find_linear_trend_line_equation(data))
    LSE2, R2_2 = LSE_and_RSquare(data, fine_square_trend_line_equation(data))
    orange_line = mlines.Line2D([],[], color="orange", label=f"Fit of degree 1, LSE = {LSE1}")
    green_line = mlines.Line2D([],[], color="green", label=f"Fit of degree 2, LSE = {LSE2}")
    red_line = mlines.Line2D([],[], color="red", label=f"Fit of degree 1, R2 = {R2_1}")
    purple_line = mlines.Line2D([],[], color="purple", label=f"Fit of degree 2, R2 = {R2_2}")
    text = [line, orange_line, green_line, red_line, purple_line]
    ax.legend(handles=text, loc="upper center")

def main():
    data = read_data(filename="oddExperiment.txt")
    fig, ax = plt.subplots()
    line = oddExperiment_scatter(data, ax)
    trend_line_dg1(data, ax)
    trend_line_dg2(data, ax)
    calculate_and_set_legent(data,ax,line)
    fig.savefig("lab12_plus.png")
    
main()
