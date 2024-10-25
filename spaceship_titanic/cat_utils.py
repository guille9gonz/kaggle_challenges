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