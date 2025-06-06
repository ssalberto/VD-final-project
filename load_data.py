import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
from constants import *

def process_storms_data():
    columns_keep = ["DURATION_HOURS", "EVENT_TYPE", "DEATHS_DIRECT", "DEATHS_INDIRECT", 
                    "INJURIES_DIRECT", "INJURIES_INDIRECT","STATE", "STATE_FIPS","YEAR"]
    df_events = pd.read_csv("./data/NOAA_StormEvents/StormEvents_2014_2024.csv")
    df_events = create_durations(df_events)
    df_events = df_events[columns_keep]
    return df_events

def process_customers_data():
    for year in range(2014, 2024):
        print(year)
        df_customers = pd.read_csv(f'./data/eaglei_data/eaglei_outages_{year}.csv')
        # df_customers['run_start_time'] = pd.to_datetime(df_customers['run_start_time'])
        df_customers = df_customers.groupby(['county', 'state', 'fips_code'])['customers_out'].sum().reset_index()
        with open(f'./data/customers_out_by_county/customers_out_{year}_bycounty.csv', 'w') as f:
            df_customers.to_csv(f, index=False)

def process_customers_data_for_time_series():
    """Agrupado por hora y estado"""
    dfs = []
    for year in range(2014, 2024):
        print(year)
        df_customers = pd.read_csv(f'./data/eaglei_data/eaglei_outages_{year}.csv')
        df_customers['run_start_time'] = pd.to_datetime(df_customers['run_start_time'])
        df_customers = df_customers.groupby(['run_start_time', 'state'])['customers_out'].sum().reset_index()

        df_customers['run_start_time'] = df_customers['run_start_time'].dt.floor('h')
        df_customers = df_customers.groupby(['run_start_time', 'state'])['customers_out'].sum().reset_index()

        dfs.append(df_customers)

    df_customers = pd.concat(dfs, ignore_index=True)
    with open(f'./data/customers_out_time_series.csv', 'w') as f:
        df_customers.to_csv(f, index=False)



def load_storm_events_data():
    df_events = pd.read_csv("./data/storms_data.csv")
    #traducir fips a nombre del estado

    # Invertimos el diccionario para mapear FIPS a abreviatura de estado
    fips_to_abbr = {v: k for k, v in STATE_ABBR_TO_STATE_FIPS.items()}
    df_events['STATE_ABB'] = df_events['STATE_FIPS'].astype(str).map(fips_to_abbr)
    df_events['STATE'] = df_events['STATE_ABB'].map(STATE_ABBR_TO_EN_NAME)
    return df_events


def load_eaglei_outages_data():
    """
    Loads customer outage data from multiple CSV files for each year.
    Returns a DataFrame with aggregated customer outage data by county.
    """
    df_list = []
    for year in range(2014, 2023):
        df_year = pd.read_csv(f'./data/customers_out_by_county/customers_out_{year}_bycounty.csv', encoding="latin1")
        df_year['YEAR'] = year
        df_year['state'] = df_year['state']
        df_list.append(df_year)
    
    df_customers = pd.concat(df_list, ignore_index=True)
    
    return df_customers

def load_data_page1():
    """
    Loads and processes data for the first page of the dashboard.
    Returns a DataFrame with storm events and customer outages data.
    """
    df_storms = load_storm_events_data()
    df_storms['state'] = df_storms['STATE']
    df_storms = df_storms.drop(columns=['STATE', 'STATE_FIPS'], errors='ignore')
    df_storms = df_storms.groupby(['state', 'YEAR']).agg(
        DURATION_HOURS=('DURATION_HOURS', 'sum'),
        EVENT_TYPE=('EVENT_TYPE', lambda x: x.mode()[0] if not x.mode().empty else 'N/A'),
        DEATHS_DIRECT=('DEATHS_DIRECT', 'sum'),
        DEATHS_INDIRECT=('DEATHS_INDIRECT', 'sum'),
        INJURIES_DIRECT=('INJURIES_DIRECT', 'sum'),
        INJURIES_INDIRECT=('INJURIES_INDIRECT', 'sum')
    ).reset_index()

    df_customers = load_eaglei_outages_data()
    df_customers = df_customers.groupby(['state', 'YEAR'])['customers_out'].sum().reset_index()

    ret = pd.merge(df_storms, df_customers, on=["state", "YEAR"], how="outer")
    return ret

def load_customers_data_for_time_series():
    """
    Loads customer outage data for time series analysis.
    Returns a DataFrame with customer outages aggregated by hour and state.
    """
    df_customers = pd.read_csv('./data/customers_out_time_series.csv')
    df_customers['run_start_time'] = pd.to_datetime(df_customers['run_start_time'])
    
    return df_customers

def load_correlation_data():
    """
    Loads correlation data for power outages and storm events.
    Returns a DataFrame with correlation coefficients.
    """
    df_correlation = pd.read_csv('./data/correlation_with_customers_out_hr.csv')
    
    return df_correlation



def create_durations(df):
    df['BEGIN_DATE'] = pd.to_datetime(
        df['BEGIN_YEARMONTH'].astype(str) + df['BEGIN_DAY'].astype(str).str.zfill(2),
        format='%Y%m%d'
    )

    df['BEGIN_DATETIME'] = pd.to_datetime(
        df['BEGIN_YEARMONTH'].astype(str) + df['BEGIN_DAY'].astype(str).str.zfill(2) + df['BEGIN_TIME'].astype(str).str.zfill(4),
        format='%Y%m%d%H%M'
    )

    df['END_DATE'] = pd.to_datetime(
        df['END_YEARMONTH'].astype(str) + df['END_DAY'].astype(str).str.zfill(2),
        format='%Y%m%d'
    )

    df['END_DATETIME'] = pd.to_datetime(
        df['END_YEARMONTH'].astype(str) + df['END_DAY'].astype(str).str.zfill(2) + df['END_TIME'].astype(str).str.zfill(4),
        format='%Y%m%d%H%M'
    )
    df['DURATION_HOURS'] = (df['END_DATETIME'] - df['BEGIN_DATETIME']).dt.total_seconds() / 3600
    
    return df
