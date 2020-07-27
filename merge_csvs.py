import pandas as pd

home_values = pd.read_csv("dopple_users_home_values.csv")
average_order_values = pd.read_csv("list_export_2020_06_30.csv")
merged = home_values.merge(average_order_values, on='email')
#merged = merged.drop(columns=['Error'])
merged.to_csv("users_by_home_value.csv", index=False)


# example of a collaborater editing an existing file
