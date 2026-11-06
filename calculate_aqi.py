"""
calculate_aqi.py
Calculates the official Central Pollution Control Board (CPCB) National Air Quality Index (AQI)
and sub-indices for PM2.5, PM10, NO2, SO2, CO, and O3.
Aggregates hourly measurements into daily averages and assigns AQI buckets.
"""

import os
import numpy as np
import pandas as pd

def calculate_sub_index(cp, breakpoints):
    """
    Generic sub-index calculator using linear interpolation across breakpoints:
    breakpoints: list of tuples ((b_low, b_high), (i_low, i_high))
    """
    if pd.isna(cp) or cp < 0:
        return np.nan
    
    for (b_low, b_high), (i_low, i_high) in breakpoints:
        if b_low <= cp <= b_high:
            return i_low + ((i_high - i_low) / (b_high - b_low)) * (cp - b_low)
            
    # If concentration exceeds highest defined breakpoint
    max_b_low, max_b_high = breakpoints[-1][0]
    max_i_low, max_i_high = breakpoints[-1][1]
    if cp > max_b_high:
        return 500.0  # CPCB cap at 500
    
    return np.nan

# Official CPCB Breakpoints
BREAKPOINTS = {
    "PM2.5": [
        ((0, 30), (0, 50)),
        ((31, 60), (51, 100)),
        ((61, 90), (101, 200)),
        ((91, 120), (201, 300)),
        ((121, 250), (301, 400)),
        ((251, 500), (401, 500))
    ],
    "PM10": [
        ((0, 50), (0, 50)),
        ((51, 100), (51, 100)),
        ((101, 250), (101, 200)),
        ((251, 350), (201, 300)),
        ((351, 430), (301, 400)),
        ((431, 600), (401, 500))
    ],
    "NO2": [
        ((0, 40), (0, 50)),
        ((41, 80), (51, 100)),
        ((81, 180), (101, 200)),
        ((181, 280), (201, 300)),
        ((281, 400), (301, 400)),
        ((401, 600), (401, 500))
    ],
    "SO2": [
        ((0, 40), (0, 50)),
        ((41, 80), (51, 100)),
        ((81, 380), (101, 200)),
        ((381, 800), (201, 300)),
        ((801, 1600), (301, 400)),
        ((1601, 2000), (401, 500))
    ],
    "CO": [
        ((0.0, 1.0), (0, 50)),
        ((1.1, 2.0), (51, 100)),
        ((2.1, 10.0), (101, 200)),
        ((10.1, 17.0), (201, 300)),
        ((17.1, 34.0), (301, 400)),
        ((34.1, 50.0), (401, 500))
    ],
    "O3": [
        ((0, 50), (0, 50)),
        ((51, 100), (51, 100)),
        ((101, 168), (101, 200)),
        ((169, 208), (201, 300)),
        ((209, 748), (301, 400)),
        ((749, 1000), (401, 500))
    ]
}

def get_aqi_bucket(aqi):
    if pd.isna(aqi):
        return "Unknown"
    elif aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

def get_season(month):
    """
    Standard Indian Meteorological Department (IMD) Seasons:
    - Winter: Jan, Feb (1, 2)
    - Summer / Pre-Monsoon: Mar, Apr, May (3, 4, 5)
    - Monsoon: Jun, Jul, Aug, Sep (6, 7, 8, 9)
    - Post-Monsoon / Autumn: Oct, Nov, Dec (10, 11, 12)
    """
    if month in [1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

def process_and_compute_aqi(input_csv="data/pollution_hourly_raw.csv", output_csv="data/pollution_daily.csv"):
    print(f"Reading {input_csv}...")
    df = pd.read_csv(input_csv)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Date"] = df["Timestamp"].dt.date
    
    # 24-hour daily aggregation (mean) per city
    pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
    meta_cols = ["State", "Elevation_m", "City_Type"]
    
    daily_df = df.groupby(["City", "Date"] + meta_cols)[pollutants].mean().reset_index()
    daily_df["Date"] = pd.to_datetime(daily_df["Date"])
    
    # Calculate sub-indices
    for poll in pollutants:
        sub_col = f"{poll}_SubIndex"
        daily_df[sub_col] = daily_df[poll].apply(lambda val: calculate_sub_index(val, BREAKPOINTS[poll]))
        
    sub_index_cols = [f"{p}_SubIndex" for p in pollutants]
    
    # Overall AQI = max(sub-indices)
    daily_df["AQI"] = daily_df[sub_index_cols].max(axis=1).round()
    
    # Identify Prominent Pollutant (the one causing the max sub-index)
    def find_prominent(row):
        valid_subs = {poll: row[f"{poll}_SubIndex"] for poll in pollutants if not pd.isna(row[f"{poll}_SubIndex"])}
        if not valid_subs:
            return "None"
        return max(valid_subs, key=valid_subs.get)

    daily_df["Prominent_Pollutant"] = daily_df.apply(find_prominent, axis=1)
    
    # Assign AQI Category
    daily_df["AQI_Bucket"] = daily_df["AQI"].apply(get_aqi_bucket)
    
    # Temporal & Seasonal features
    daily_df["Year"] = daily_df["Date"].dt.year
    daily_df["Month"] = daily_df["Date"].dt.month
    daily_df["Month_Name"] = daily_df["Date"].dt.strftime("%b")
    daily_df["Day"] = daily_df["Date"].dt.day
    daily_df["DayOfWeek"] = daily_df["Date"].dt.day_name()
    daily_df["Is_Weekend"] = daily_df["Date"].dt.dayofweek.isin([5, 6]).astype(int)
    daily_df["Season"] = daily_df["Month"].apply(get_season)
    
    # Round pollutant concentrations for clean presentation
    for poll in pollutants:
        daily_df[poll] = daily_df[poll].round(2)
        daily_df[f"{poll}_SubIndex"] = daily_df[f"{poll}_SubIndex"].round(1)
        
    daily_df.to_csv(output_csv, index=False)
    print(f"[SUCCESS] Processed {len(daily_df)} daily records across 4 cities.")
    print(f"Saved to: {output_csv}")
    
    # Print sample distribution
    print("\nAQI Bucket distribution by city:")
    print(pd.crosstab(daily_df["City"], daily_df["AQI_Bucket"]))
    
    return daily_df

if __name__ == "__main__":
    process_and_compute_aqi()
