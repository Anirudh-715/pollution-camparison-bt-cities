"""
fetch_data.py
Fetches high-resolution historical air quality data from the Open-Meteo Air Quality API
for Delhi, Chandigarh, Shimla, and Solan.
"""

import os
import requests
import pandas as pd
from datetime import datetime

# Coordinates and Metadata for the 4 cities
CITIES_CONFIG = {
    "Delhi": {
        "latitude": 28.6139,
        "longitude": 77.2090,
        "state": "Delhi",
        "elevation_m": 216,
        "type": "Megacity / Capital (Plains)"
    },
    "Chandigarh": {
        "latitude": 30.7333,
        "longitude": 76.7794,
        "state": "Chandigarh UT",
        "elevation_m": 321,
        "type": "Planned Urban (Foothills)"
    },
    "Solan": {
        "latitude": 30.9045,
        "longitude": 77.0967,
        "state": "Himachal Pradesh",
        "elevation_m": 1502,
        "type": "Industrial / Transit Belt (Mid-Hills)"
    },
    "Shimla": {
        "latitude": 31.1048,
        "longitude": 77.1734,
        "state": "Himachal Pradesh",
        "elevation_m": 2276,
        "type": "Tourist / Hill Station (High-Altitude)"
    }
}

API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

def fetch_city_air_quality(city_name, config, start_date="2023-01-01", end_date="2023-12-31"):
    print(f"Fetching data for {city_name} ({start_date} to {end_date})...")
    params = {
        "latitude": config["latitude"],
        "longitude": config["longitude"],
        "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone",
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "Asia/Kolkata"
    }
    
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    
    hourly = data.get("hourly", {})
    df = pd.DataFrame(hourly)
    
    # Rename columns to standard scientific names
    df.rename(columns={
        "pm2_5": "PM2.5",
        "pm10": "PM10",
        "carbon_monoxide": "CO",
        "nitrogen_dioxide": "NO2",
        "sulphur_dioxide": "SO2",
        "ozone": "O3"
    }, inplace=True)
    
    # Metadata columns
    df["City"] = city_name
    df["State"] = config["state"]
    df["Elevation_m"] = config["elevation_m"]
    df["City_Type"] = config["type"]
    
    # Datetime features
    df["time"] = pd.to_datetime(df["time"])
    df.rename(columns={"time": "Timestamp"}, inplace=True)
    
    return df

def main():
    os.makedirs("data", exist_ok=True)
    all_data = []
    
    for city, config in CITIES_CONFIG.items():
        city_df = fetch_city_air_quality(city, config, start_date="2023-01-01", end_date="2023-12-31")
        all_data.append(city_df)
    
    combined_hourly = pd.concat(all_data, ignore_index=True)
    
    # Open-Meteo returns CO in ug/m3. In CPCB standards, CO is measured in mg/m3.
    # Convert CO from ug/m3 to mg/m3: 1 mg = 1000 ug
    combined_hourly["CO"] = combined_hourly["CO"] / 1000.0
    
    raw_path = os.path.join("data", "pollution_hourly_raw.csv")
    combined_hourly.to_csv(raw_path, index=False)
    print(f"\n[SUCCESS] Successfully fetched {len(combined_hourly)} hourly records.")
    print(f"Saved to: {raw_path}")

if __name__ == "__main__":
    main()
