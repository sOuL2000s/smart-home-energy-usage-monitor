import pandas as pd

# Sample data for appliances and their daily energy consumption (kWh)
energy_data = {
    "Appliance": ["Air Conditioner", "Refrigerator", "Washing Machine", "Heater", "Television"],
    "DailyUsage_kWh": [2.5, 1.0, 0.8, 3.0, 0.5]
}

# Convert to DataFrame
df = pd.DataFrame(energy_data)

# Calculate monthly usage for each appliance
df["MonthlyUsage_kWh"] = df["DailyUsage_kWh"] * 30

# Identify high-energy appliances (threshold example: >50 kWh per month)
high_energy_appliances = df[df["MonthlyUsage_kWh"] > 50]
print("High-energy appliances (over 50 kWh/month):")
print(high_energy_appliances)

# Total monthly energy usage
total_usage = df["MonthlyUsage_kWh"].sum()
print(f"\nTotal monthly energy usage: {total_usage} kWh")
