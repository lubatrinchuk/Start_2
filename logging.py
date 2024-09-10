import pandas as pd
from datetime import datetime

def logging(filename, event):
    file = 'Журнал.xlsx'
    df_orders = pd.read_excel(file, skiprows=0, index_col=0)
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    new = {'Время': current_time, 'Файл': filename, 'Событие': event}
    df_orders_new = pd.DataFrame([new])
    df_orders_new.index = [current_date]
    df_results = pd.concat([
        df_orders,
        df_orders_new
    ])
    df_results.to_excel('Журнал.xlsx')