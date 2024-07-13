import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# 讀取檔案和過濾資料
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

# 繪製散佈圖和設定標題、軸的文字
def oddExperiment_scatter(data, ax):
    x_ticks = np.arange(-10.0, 10.1, 2.5)
    ax.set_title("oddExperiment Data")
    ax.set_xticks(x_ticks)

    x, y = data
    
    line = ax.scatter(x, y, label="Data")
    return line

# 計算一次趨勢線的方程式, 並回傳
def find_linear_trend_line_equation(data):
    x, y = data
    coefficients = np.polyfit(x, y, 1)
    return np.poly1d(coefficients)

# 計算二次趨勢線的方程式, 並回傳
def fine_square_trend_line_equation(data):
    x, y = data
    coefficients = np.polyfit(x, y, 2)
    return np.poly1d(coefficients)

# 繪製一次趨勢線的圖形
def trend_line_dg1(data, ax):
    x = np.linspace(-10.0, 10.0, 100)
    func = find_linear_trend_line_equation(data)
    y = func(x) 
    ax.plot(x, y, color="red")

# 繪製二次趨勢線的圖形
def trend_line_dg2(data, ax):
    x = np.linspace(-10.0, 10.0, 100)
    func = fine_square_trend_line_equation(data)
    y = func(x)
    ax.plot(x, y, color="purple")

# 計算 LSE, 並且回傳數值
def LSE_and_RSquare(data, equation):
    x_p, y_p = data
    y_i = equation(x_p)
    diff_square = (y_i - y_p)**2
    LSE = np.mean(diff_square)
    # mean = np.mean(y_p)
    # RSquare = 1 - (np.sum(diff_square)/np.sum((y_p-mean)**2))
    return np.around(LSE, 5)

# 計算 LSE 和設定 legend
def calculate_and_set_legend(data, ax, line):
    # 計算一次趨勢線的 LSE
    LSE1 = LSE_and_RSquare(data, find_linear_trend_line_equation(data))
    # 計算二次趨勢線的 LSE
    LSE2 = LSE_and_RSquare(data, fine_square_trend_line_equation(data))
    # 繪製 legend
    orange_line = mlines.Line2D([],[], color="orange", label=f"Fit of degree 1, LSE = {LSE1}")
    green_line = mlines.Line2D([],[], color="green", label=f"Fit of degree 2, LSE = {LSE2}")
    # red_line = mlines.Line2D([],[], color="red", label=f"Fit of degree 1, R2 = {R2_1}")
    # purple_line = mlines.Line2D([],[], color="purple", label=f"Fit of degree 2, R2 = {R2_2}")
    text = [line, orange_line, green_line]
    ax.legend(handles=text, loc="upper center")

def main():
    # 進行資料處理
    data = read_data(filename=r"E94126169_Lab12\data\oddExperiment.txt")
    # 創造子圖
    fig, ax = plt.subplots()
    # 繪製散佈圖
    line = oddExperiment_scatter(data, ax)
    # 繪製一次趨勢線
    trend_line_dg1(data, ax)
    # 繪製二次趨勢線
    trend_line_dg2(data, ax)
    # 計算 LSE 和製作 legend
    calculate_and_set_legend(data,ax,line)
    # 儲存圖檔
    fig.savefig(r"E94126169_Lab12\lab12_plus.png")
    
main()
