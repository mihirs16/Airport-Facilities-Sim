import pandas as pd
import numpy as np
import datetime as dt
import random
from datetime import datetime, timedelta

total_data = 100    #Needed length
total_loco_id = 4   #Needed No. of locomotives

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

id_lst = []
st_lst = []
for i in range(0, total_data):
    id_lst.append(random.randint(1, total_loco_id))
    st_lst.append(random.randint(0, 2))
ti_lst = gen_datetime(min_year=2020, length=total_data)
loco_df = pd.DataFrame(data = {"Loco_id":id_lst, "State_Change":ti_lst, "Curr_State":st_lst})

# print(loco_df)
loco_df.to_csv('inloco_data_mock.csv')