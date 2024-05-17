import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Imbalance.csv'
data = pd.read_csv(file_path)

imbalance_column_name = 'Total Imbalance [MWh] - SCA|FR'

imbalance_data = pd.to_numeric(data[imbalance_column_name], errors='coerce').dropna().values
print(len(imbalance_data))

# Sort the data to calculate the cumulative probability
sorted_data = np.sort(imbalance_data)

def compute_lolp(reserve, sorted_imbalance_data):
    # Probability of an imbalance higher than the given reserve
    return np.mean(sorted_imbalance_data > reserve)

reserve_range = np.linspace(0, max(sorted_data), 100)

lolp_values = [compute_lolp(R, sorted_data) for R in reserve_range]

VOLL = 5000  

ordc_values = np.array(lolp_values) * VOLL

# Plot the ORDC curve
plt.figure(figsize=(8, 6))
plt.plot(reserve_range, ordc_values, label='ORDC', color='blue')
plt.xlabel('Reserve (MW)')
plt.ylabel('ORDC Value ($)')
plt.title('Operating Reserve Demand Curve (ORDC)')
plt.legend()
plt.grid(visible=True)
plt.show()
