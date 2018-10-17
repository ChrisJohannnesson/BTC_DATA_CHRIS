import bitmex 
import matplotlib.pyplot as plt 
from matplotlib import style
import datetime 
import pandas as pd
import pandas_datareader.data as web 
import numpy as np

style.use('ggplot')

#DATA 
client = bitmex.bitmex()
start = client.Quote.Quote_get(symbol="XBTUSD", startTime=datetime.datetime(2018,1,1)).result()
end = client.Quote.Quote_get(symbol="XBTUSD", endTime=datetimet.datetime.utcnow).result()

df = web.DataReader("XBTUSD", start,end)

df.head()
