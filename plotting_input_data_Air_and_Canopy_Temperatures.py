import numpy as np
import matplotlib.pyplot as plt

# Create latitude/longitude grid
lon = np.linspace(75.1498, 75.1502, 100)  
lat = np.linspace(39.9498, 39.9502, 100)

longitude, latitude = np.meshgrid(lon, lat)

# Define constant input data 
datetime = 648857.5
alb_soil = 0.105
alb_veg = 0.2
emiss_soil = 0.945
emiss_veg = 0.94
pa = 101.3
LAI = 2.5
h = 1.5
SW_in = 700
u = 4.75
ea = 2.25

# Define variable input data
T_air = 25 + np.random.randn(*longitude.shape)  

X, Y = np.meshgrid(np.linspace(10,15,50), np.linspace(10,15,50)) 
T = X + Y

# Plot input data
fig, axs = plt.subplots(1, 2, figsize=(10,5))

im = axs[0].pcolormesh(T_air, cmap='RdBu_r')
axs[0].set_title('Air Temperature [C]')
fig.colorbar(im, ax=axs[0])

im = axs[1].pcolormesh(T, cmap='RdBu_r')
axs[1].set_title('Canopy Temperature [C]')
fig.colorbar(im, ax=axs[1])

plt.tight_layout()
plt.show()

# Save data
data = {'longitude': longitude, 'latitude': latitude,  
        'T_air': T_air, 'T': T}
        
np.savez('moscow_idaho_data.npz', **data)
