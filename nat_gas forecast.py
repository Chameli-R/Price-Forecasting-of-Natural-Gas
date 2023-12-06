# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:41:14 2023

@author: CHAMELI RAMESH
"""

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
data = pd.read_csv('Nat_Gas.csv')
data['Dates']=pd.to_datetime(data['Dates'])
data.set_index('Dates', inplace=True)
seasonal_periods=12
model = ExponentialSmoothing(data, trend='mul', seasonal='mul', seasonal_periods=seasonal_periods)
result = model.fit()
input_date = pd.to_datetime(input("Enter a date (YYYY-MM-DD): "))
forecast_horizon=12
forecast=result.forecast(forecast_horizon)
print("Forecasted value for", input_date.date(), "is", forecast[0])