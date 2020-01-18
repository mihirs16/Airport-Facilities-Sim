import pandas as pd
import numpy as np
import datetime as dt
import random
from datetime import datetime, timedelta

#Needed length
total_park_data = 100

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

def gen_datetime(min_year=2019, max_year=datetime.now().year, length=20):
    lst = []
    for i in range(0, length):
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        lst.append(start + (end - start) * random.random())
        lst.sort()
        i = i + 1
    return lst

park_gen_car_id = np.arange(1, (total_park_data + 1))
park_gen_entry = gen_datetime(min_year=2020, length=total_park_data)

park_gen_entry_exit_delta_hrs = np.random.normal(5, 5.0, size=total_park_data)
park_gen_entry_exit_delta_day = np.random.normal(2, 1.0, size=total_park_data)

park_gen_exit = []
for i in range(0, total_park_data):
    x = park_gen_entry[i] + timedelta(hours=park_gen_entry_exit_delta_hrs[i])
    y = park_gen_entry[i] + timedelta(days=park_gen_entry_exit_delta_day[i])
    park_gen_exit.append(x if random.randint(0, 1) else y)

park_df = pd.DataFrame(data={'Car_ID':park_gen_car_id, 'Entry':park_gen_entry, 'Exit':park_gen_exit})
park_df.set_index(park_gen_car_id, inplace=True)

#To add DIFFERENCE BETWEEN ENTRY & EXIT TIME 
'''
park_gen_delta = []
for x, y in zip(park_gen_entry, park_gen_exit):
    diff = (y - x).days
    if diff < 0:
        y = y + timedelta(days=(-diff))
    park_gen_delta.append((y-x).days)
park_df["Delta"] = park_gen_delta
'''

#print(park_df)

park_df.to_csv('parking_data_mock.csv')