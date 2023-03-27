import pandas as pd
import matplotlib.pyplot as plt
import requests

api = 'VQ568JQI6OMF0VX4'

while True:
  try:
    company = input("Enter the ticker symbol for the company: ").capitalize()
    start = input("Enter the start date in the format yyyy-mm-dd: ")
    end = input("Enter the end date in the format yyyy-mm-dd: ")

    # Getting data of the stock
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+company+'&apikey='+ api
    r = requests.get(url)
    data = r.json()
    data.pop('Meta Data')

    # Making a dataframe
    df = pd.DataFrame.from_dict(data['Weekly Time Series'], orient='index')

    # Rename the column names to remove the prefix
    df = df.rename(columns=lambda x: x[3:])

    # Convert the column data types to float
    df = df.astype(float)

    df = df.loc[end:start]

    # Plotting the Weekly Volumes
    plt.figure(figsize=(20, 5))
    plt.plot(df['volume'])
    plt.ylabel("Value (10 Millions)")
    plt.xlabel("Date")
    plt.title("Weekly Volumes")
    plt.show()

    # Plotting the weekly Stock Prices
    plt.figure(figsize=(20, 5))
    plt.plot(df['open'])
    plt.plot(df['high'])
    plt.plot(df['low'])
    plt.plot(df['close'])
    plt.ylabel("Value")
    plt.xlabel("Date")
    plt.title("Weekly Stock Prices")
    plt.legend(['open', 'high', 'low', 'close'])
    plt.show()

    break
  except:
    print("Invalid data entered")



