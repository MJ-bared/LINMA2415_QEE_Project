import json
import matplotlib.pyplot as plt
import numpy as np

with open("capacity_data.txt", "r") as file:
    capacity_data = json.load(file)

technologies = ["Coal", "CCGT", "OCGT", "Onshore Wind", "Offshore Wind", "PV"]
carbon_tax_levels = np.arange(0, 501, 20) 

fig, ax = plt.subplots()

bottom = np.zeros(len(carbon_tax_levels))

for tech in technologies:
    ax.bar(carbon_tax_levels, capacity_data[tech], bottom=bottom, label=tech, width=18)
    bottom += np.array(capacity_data[tech]) 

ax.set_title("Optimal Capacity Mix vs. Carbon Tax")
ax.set_xlabel("Carbon Tax")
ax.set_ylabel("Capacity (MW)")
ax.set_xticks(carbon_tax_levels)  
ax.set_xticklabels(carbon_tax_levels, rotation=45)  
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))  

#plt.savefig("capacity_mix_vs_carbon_tax2.png")
plt.show()
