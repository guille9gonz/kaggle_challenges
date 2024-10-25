import numpy as np
import pandas as pd

def handle_num_cols(df):
    # Calculate a new column for the total amount spent within all services
    df['Billed'] = df['RoomService'] + df['FoodCourt'] + df['ShoppingMall'] + df['Spa'] + df['VRDeck']

    # Fill NaN based on the bill
    billed_min = round(df['Billed'].mean(), 2)
    billed_max = round(df[df['Billed'] != 0]['Billed'].mean(), 2)
    nan_bill = df['Billed'].isna()

    # Applies max amount if condition is satisfied (> 0) and min amount if not (0)
    replace_bill = np.where(df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].gt(0).any(axis=1),
                        billed_min,
                        billed_max)
    df.loc[nan_bill, 'Billed'] = replace_bill[nan_bill]

    return df

def fillna_bills(row):
    target = row['Billed']
    num_cols = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    num_sum = row[num_cols].sum(skipna=True) # Sum of non NaN values
    row[num_cols] = row[num_cols].fillna((target - num_sum)/row[num_cols].isna().sum())
    return row

def fillna_age(df):
    mean_age = df['Age'].mean()
    df['Age'].fillna(mean_age, inplace=True)
    return df