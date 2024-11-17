#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask pandas plotly


# In[ ]:


import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# Initialize an empty DataFrame to store sensor data
data = pd.DataFrame(columns=["timestamp", "temperature", "pressure", "vibration"])

# Function to simulate data
def generate_data():
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    temperature = random.uniform(50, 100)  # Simulated temperature (Celsius)
    pressure = random.uniform(100, 200)   # Simulated pressure (kPa)
    vibration = random.uniform(0.5, 2.0)  # Simulated vibration (m/s^2)
    return current_time, temperature, pressure, vibration

# Function to detect anomalies
def detect_anomalies(temp, press, vib):
    anomalies = []
    if temp > 80:
        anomalies.append("High Temperature")
    if press > 150:
        anomalies.append("High Pressure")
    if vib > 1.5:
        anomalies.append("High Vibration")
    return anomalies

# Function to update and plot data
def update_and_plot(data):
    plt.clf()  # Clear the previous plot

    # Plot each metric
    plt.plot(data["timestamp"], data["temperature"], label="Temperature (°C)", color="red")
    plt.plot(data["timestamp"], data["pressure"], label="Pressure (kPa)", color="blue")
    plt.plot(data["timestamp"], data["vibration"], label="Vibration (m/s²)", color="green")
    
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Real-Time Sensor Data")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.pause(1)  # Pause to update the plot

# Main loop to generate and visualize data
plt.ion()  # Turn on interactive mode for Matplotlib
print("Starting real-time data simulation... (Press Ctrl+C to stop)")

try:
    while True:
        # Generate a new data point
        timestamp, temperature, pressure, vibration = generate_data()
        anomalies = detect_anomalies(temperature, pressure, vibration)

        # Print anomalies, if any
        if anomalies:
            print(f"Anomalies at {timestamp}: {', '.join(anomalies)}")

        # Create a new row and add it to the DataFrame
        new_row = pd.DataFrame({
            "timestamp": [timestamp],
            "temperature": [temperature],
            "pressure": [pressure],
            "vibration": [vibration]
        })
        data = pd.concat([data, new_row], ignore_index=True)

        # Keep the DataFrame size manageable (e.g., last 20 points)
        if len(data) > 20:
            data = data.iloc[1:]

        # Update the plot
        update_and_plot(data)

        # Wait for a second before generating the next data point
        time.sleep(1)

except KeyboardInterrupt:
    print("Simulation stopped.")
    plt.ioff()  # Turn off interactive mode
    plt.show()


# In[ ]:




