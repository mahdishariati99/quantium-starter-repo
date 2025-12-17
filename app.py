import pandas as pd
 
#read all csv files in the directory
data1= pd.read_csv('data/daily_sales_data_0.csv')
data2= pd.read_csv('data/daily_sales_data_1.csv')
data3= pd.read_csv('data/daily_sales_data_2.csv')

#merge all data into single file
merged_data = pd.concat([data1,data2,data3], ignore_index=True)

#save merged data to csv
merged_data.to_csv('merged_data.csv', index=False)

#filter pink_morsel data
pink_morsel_data = merged_data[merged_data['product'] == 'pink morsel']

#clean price column
pink_morsel_data['price'] = pink_morsel_data['price'].str.replace('$', '').astype(float)

#calculate sales
pink_morsel_data['sales'] = pink_morsel_data['price'] * pink_morsel_data['quantity']

#keeping 3 columns
pink_morsel_data = pink_morsel_data[['date', 'region', 'sales']]

#save pink_morsel_data to csv
pink_morsel_data.to_csv('pink_morsel_data.csv', index=False)
