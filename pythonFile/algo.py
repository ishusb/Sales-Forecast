import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import csv
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from matplotlib import rcParams
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from pandas.tseries.offsets import DateOffset
import cv2

 
def code(file,value):
    df=pd.read_csv(file)
    df.columns=["Month","Sales"]
    df.dropna(how="any",inplace=True,axis='index',subset=['Month','Sales'])
    df.drop_duplicates(inplace = True)
    df['Month']=pd.to_datetime(df['Month'])
    df.set_index('Month',inplace=True)


    test_result=adfuller(df['Sales'])
    def adfuller_test(sales):
        result=adfuller(sales)
        labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
        for value,label in zip(result,labels):
            print(label+' : '+str(value) )
        if result[1] <= 0.05:
            print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
        else:
            print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
    test_result=adfuller_test(df['Sales'])
    print(test_result)


    df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)
    #df['Seasonal First Difference'].plot()
    autocorrelation_plot(df['Sales'])
    #plt.show()
    model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
    results=model.fit()
    df['forecast']=results.predict(start=90,end=103,dynamic=True)
    #df[['Sales','forecast']].plot(figsize=(12,8))
    if(value==0):
        future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,12)]
        future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
        future_df=pd.concat([df,future_datest_df])
        future_df['forecast'] = results.predict(start = 104, end = 116, dynamic= True) 
    if(value==1):
        future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]
        future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
        future_df=pd.concat([df,future_datest_df])
        future_df['forecast'] = results.predict(start = 104, end = 128, dynamic= True)
    if(value==2):
        future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,48)]
        future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
        future_df=pd.concat([df,future_datest_df])
        future_df['forecast'] = results.predict(start = 104, end = 152, dynamic= True)   
    future_df[['Sales', 'forecast']].plot(figsize=(12, 8)) 

    
    plt.plot()
    plt.savefig('plot.jpg')
    image = cv2.imread('plot.jpg')
    path = r"C:\Users\Ishwarya\salesAPP\src\assets"
    (cv2.imwrite(os.path.join(path,'plot.jpg'), image))


    return future_df


    
    








