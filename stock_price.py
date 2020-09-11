import requests

site = "https://query1.finance.yahoo.com/v8/finance/chart/GT?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
response = requests.get(site)
response.text[:1000]

import json
import numpy as np
import pandas as pd
import datetime

data = json.loads(response.text)
df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
df.head()