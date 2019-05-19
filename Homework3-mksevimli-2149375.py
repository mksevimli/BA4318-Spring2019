#Question_1
import pandas as pd
import matplotlib.pyplot as plt

data_file = 'HW03_USD_TRY_Trading.txt'

data = pd.read_csv(data_file, delimiter='\t')



def check_entire_stationarity_mean():

    plot = data.High.rolling(window=50).mean()
    plot2 = data.Low.rolling(window=50).mean()

    plt.plot(plot, label="High Values", color = 'red')
    plt.plot(plot2, label="Low Values",color = 'blue')
    plt.legend(loc='upper left')
    plt.title("check_entire_stationarity_mean")
    plt.show()

def check_entire_stationarity_std_deviation():

    plot = data.High.rolling(window=50).std()
    plot2 = data.Low.rolling(window=50).std()

    plt.plot(plot, label="High Values", color = 'red')
    plt.plot(plot2, label="Low Values",color = 'blue')
    plt.legend(loc='upper left')
    plt.title("check_entire_stationarity_std_deviation")
    plt.show()

def check_may_6th_stationary_mean():

    begin_index = 0

    for i in range(len(data)):
        if(data.Day[i] == '6.05.2019'):
            begin_index = i
            break
    plot = data.High[begin_index:len(data)].rolling(window=50).mean()
    plot2 = data.Low[begin_index:len(data)].rolling(window=50).mean()
    plt.plot(plot, label="High Values", color = 'red')
    plt.plot(plot2, label="Low Values",color = 'blue')
    plt.legend(loc='upper left')
    plt.title("check_may_6th_stationary_mean")
    plt.show()
def check_may_6th_stationary_std_deviation():

    begin_index = 0

    for i in range(len(data)):
        if(data.Day[i] == '6.05.2019'):
            begin_index = i
            break
    plot = data.High[begin_index:len(data)].rolling(window=50).std()
    plot2 = data.Low[begin_index:len(data)].rolling(window=50).std()
    plt.plot(plot, label="High Values", color = 'red')
    plt.plot(plot2, label="Low Values",color = 'blue')
    plt.legend(loc='upper left')
    plt.title("check_may_6th_stationary_std_deviation")
    plt.show()





check_entire_stationarity_mean()
check_entire_stationarity_std_deviation()

check_may_6th_stationary_mean()
check_may_6th_stationary_std_deviation()

#Question_2
df2 = df.iloc[::60]
df3 = df.iloc[59::60]
df_all_rows = pd.concat([df2, df3])
###discard rows with no trading data
df_all_rows = df_all_rows[~(df == 0).any(axis=1)]
df_all_rows = df_all_rows.dropna()
print(df_all_rows)
    
seriesname = "Close"
series = df_all_rows[seriesname]
test_stationarity(series)
print(calculate_everything(df_all_rows))
    
#smoothing by a simple -one-sided- moving average
df = df.set_index(["Day","Time"])
smoothed_data = df.rolling(window=60).mean()
smoothed_data = smoothed_data.dropna()
#print(smoothed_data.head(61))
calculate_everything(smoothed_data)
df = df.reset_index(["Day","Time"])
seriesname = "Close"
series = df[seriesname]
test_stationarity(series)
print(series.tail())

#A random pick from each hour
df2 = (df.sample(n= 10))
calculate_everything(df2)
seriesname = "Close"
series = df2[seriesname]
test_stationarity(series)
print(series.tail())