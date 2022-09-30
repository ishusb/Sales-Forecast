import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def errorC(file):
    future_df=pd.read_csv(file)
    future_df.columns=["Month","Sales","Seasonal First Difference","forecast"]
    future_df.dropna(how="any",inplace=True,axis=0)
    future_df.drop_duplicates(inplace = True)
    def me(f,y):
        f = f.reset_index(drop=True).values.flatten()
        y = y.reset_index(drop=True).values.flatten()
        df = pd.DataFrame({'f_i':f, 'y_i': y})
        df['e'] = df['y_i'] - df['f_i']
        return np.mean(df['e'])
        
    meanError=me(future_df['Sales'],future_df['forecast'])
    print("Mean Error is " + str(meanError))

    def mae(f, y):
        f = f.reset_index(drop=True).values.flatten()
        y = y.reset_index(drop=True).values.flatten()
        df = pd.DataFrame({'f_i':f, 'y_i': y})
        df['e'] = np.abs(df['y_i'] - df['f_i'])
        return np.mean(df['e'])

    meanAbsError=mae(future_df['Sales'],future_df['forecast'])
    print("Mean Absolute Error is " + str(meanAbsError))

    def mse(f, y):
        f = f.reset_index(drop=True).values.flatten()
        y = y.reset_index(drop=True).values.flatten()
        df = pd.DataFrame({'f_i':f, 'y_i': y})
        df['e'] = np.square(df['y_i'] - df['f_i'])
        return np.mean(df['e'])

    def rmse(f, y):
        return np.sqrt(mse(f,y))

    rootMeansqrError=rmse(future_df['Sales'],future_df['forecast'])
    print("Root Mean Square Error is " + str(rootMeansqrError))

    def mape(f, y):
        f = f.reset_index(drop=True).values.flatten()
        y = y.reset_index(drop=True).values.flatten()
        df = pd.DataFrame({'f_i':f, 'y_i': y})
        df['e'] = df['y_i'] - df['f_i']
        df['ape'] = 100*np.abs(df['e']/df['y_i'])
        return np.mean(df['ape'])

    meanabsperError=mape(future_df['Sales'],future_df['forecast'])
    print("Mean Absolute Percentage Error is " + str(meanabsperError))

    def u1(f,y):
        y = y.reset_index(drop=True).values.flatten()
        f = f.reset_index(drop=True).values.flatten()
        df = pd.DataFrame({'f_i':f, 'y_i': y})
        df['(f_i - y_i)^2'] = np.square(df['f_i'] - df['y_i'])
        df['y_i^2'] = np.square(df['y_i'])
        df['f_i^2'] = np.square(df['f_i'])
        return (np.sqrt(np.mean(df['(f_i - y_i)^2'])))/(np.sqrt(np.mean(df['y_i^2']))+np.sqrt(np.mean(df['f_i^2'])))

    theilUStats=u1(future_df['Sales'],future_df['forecast'])
    print("Theils U statistics " + str(theilUStats))

    # def u2(f,y):
    #     y = y.reset_index(drop=True).values.flatten()
    #     f = f.reset_index(drop=True).values.flatten()
    #     df = pd.DataFrame({'f_i+1':f, 'y_i+1': y})
    #     df['y_i'] = df['y_i+1'].shift(periods=1)
    #     df['numerator'] = np.square((df['f_i+1'] - df['y_i+1']) / df['y_i'])
    #     df['denominator'] = np.square((df['y_i+1'] - df['y_i']) / df['y_i'])
    #     return np.sqrt(np.sum(df['numerator'])/np.sum(df['denominator']))

    # theilUStats1=u2(future_df['Sales'],future_df['forecast'])
    # print("Theils U statistics " + str(theilUStats1))

    dict={"Mean Absolute Error":meanAbsError, "Root Mean Squre Error":rootMeansqrError,"Mean Absolute Percentage Error":meanabsperError,"Theil's U Statistic": theilUStats}
    # dict=dict.items()
    # dict=list(dict)
    # dict=np.array(dict)
    

    return dict


        