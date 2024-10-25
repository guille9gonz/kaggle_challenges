import numpy as np
import pandas as pd

def home_destin(df):
    # Create new column with the route (home - destination)
    df['Route'] = df['HomePlanet'].fillna('Unknown') + "_" + df['Destination'].fillna('Unknown')

    # Fill with the most common home/destination for each route
    routes = ['Unknown_TRAPPIST-1e', 'Earth_Unknown', 'Mars_Unknown', 'Europa_Unknown', 'Unknown_55 Cancri e', 'Unknown_PSO J318.5-22', 'Unknown_Unknown']
    for route in routes:
        if route in ['Unknown_TRAPPIST-1e', 'Earth_Unknown', 'Unknown_Unknown']:
            df.loc[df['Route'] == route, 'Route'] = 'Earth_TRAPPIST-1e'
        elif route == 'Mars_Unknown':
            df.loc[df['Route'] == route, 'Route'] = 'Mars_TRAPPIST-1e'
        elif route == 'Europa_Unknown':
            df.loc[df['Route'] == route, 'Route'] = 'Europa_TRAPPIST-1e'
        elif route == 'Unknown_55 Cancri e':
            df.loc[df['Route'] == route, 'Route'] = 'Europa_55 Cancri e'
        elif route == 'Unknown_PSO J318.5-22':
            df.loc[df['Route'] == route, 'Route'] = 'Mars_PSO J318.5-22'
    return df


def vip(df):
    # Fill VIP with the most common (False, by a huge difference)
    mode_vip = df['VIP'].mode()[0]
    df['VIP'].fillna(mode_vip, inplace=True)

    # Convert to int
    df['VIP'] = df['VIP'].astype(int)

    return df


def cryo_sleep(df):
    df_mode_cryo = df.groupby('Route')['CryoSleep'].agg(lambda x: x.mode()[0])

    # Fill NaN in Cryo with the most common bool based on the route
    df['CryoSleep'] = df.apply(
        lambda row: df_mode_cryo[row['Route']] if pd.isna(row['CryoSleep'])
        else row['CryoSleep'],
        axis=1)

    # Convert to int
    df['CryoSleep'] = df['CryoSleep'].astype(int)

    return df


def name(df):
    df['Name'].fillna('Unknown', inplace=True)

    # Create separated column for surnames only
    df['Surname'] = df['Name'].apply(lambda x: str(x).split()[-1])

    return df


def cabin(df):
    # Fill NaN based on Surname
    df_surname_cabin = df.dropna(subset=['Cabin']).groupby('Surname')['Cabin'].first()
    df['Cabin'] = df['Cabin'].fillna(df['Surname'].map(df_surname_cabin))
    df['Cabin'] = df['Cabin'].fillna('Unknown')
    df['Cabin'] = df['Cabin'].replace('Unknown', 'Unknown/Unknown/Unknown')

    # Split Cabin into Deck, Number and Side
    df[['Cabin_deck', 'Cabin_num', 'Cabin_side']] = df['Cabin'].str.split('/', expand=True)

    return df