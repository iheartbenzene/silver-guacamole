import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import matplotlib.dates as mdates

headers = ['Sensor Value', 'Date', 'Time']
df = pd.read_csv('G:\python\python_3_7_1\lpthw\DATA.CSV', names = headers)
print(df)

df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x),
                            '%Y/%m/%d %H:%M:%S.%f'))
x = df['Date']
y = df['Sensor Value']

plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()
