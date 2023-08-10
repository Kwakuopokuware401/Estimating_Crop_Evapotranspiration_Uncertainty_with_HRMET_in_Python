import numpy as np 
import matplotlib.pyplot as plt

# Define a simple HRMET model function 
# Taking longitude, latitude, air temp, and canopy temp as inputs
# Returns ET rate in mm/hr
def HRMET(lon, lat, tair, tcanopy):

  # Model calculates ET as function of temp difference 
  return 0.5 + 0.1 * (tair - tcanopy)

# Load input data from a saved NumPy array
data = np.load('moscow_idaho_data.npz') 

# Extract input arrays from the data file
lons = data['lons']  
lats = data['lats']
tair = data['tair']
t = data['t']

# Initialize output ET array  
et = np.full_like(lons, np.nan)

# Loop through each lat/lon and calculate ET 
for i in range(len(lats)):
  for j in range(len(lons)):
    
    # Pass scalar values to HRMET model
    et[i,j] = HRMET(lons[i,j], lats[i,j], 
                    tair[i,j], t[i,j])
                    
# Visualize the results
fig, axs = plt.subplots(1, 3, figsize=(12,4))

# Show air temp map
axs[0].imshow(tair, cmap='jet')  
axs[0].set_title('Air Temp [C]')

# Show canopy temp map 
axs[1].imshow(t, cmap='jet')
axs[1].set_title('Canopy Temp [C]')

# Show resulting ET rate map
axs[2].imshow(et, cmap='jet', vmin=0, vmax=1) 
axs[2].set_title('ET Rate [mm/hr]')

# Layout and display plots
plt.tight_layout()
plt.show()
