import numpy as np
import matplotlib.pyplot as plt

# HRMET model 
def HRMET(lon, lat, tair, tcanopy):
  return 0.5 + 0.1 * (tair - tcanopy)

# Generate random input data
lons = np.random.randn(50, 50)
lats = np.random.randn(50, 50)

tair = 15 + 5 * np.random.rand(50, 50)
t = 10 + 10 * np.random.rand(50, 50)

# Estimate uncertainty with moving window
tair_mean, tair_std = moving_window(tair, 5)

# Estimate uncertainty with regression  
n = 100
tair_uncertain = np.zeros((n, 50, 50))
for i in range(n):
  coef = np.random.rand(4) - 0.5
  tair_uncertain[i] = tair + coef[0]*tair + coef[1]*t + coef[2]*lons + coef[3]*lats

tair_reg_mean = np.mean(tair_uncertain, axis=0) 
tair_reg_std = np.std(tair_uncertain, axis=0)

# Estimate uncertainty in met data
tair_met = np.random.normal(tair, 1)

# Plot uncertainty maps 
fig, axs = plt.subplots(1, 3, figsize=(16,5))

axs[0].set_title('Moving Window')
axs[0].imshow(tair_std)

axs[1].set_title('Regression') 
axs[1].imshow(tair_reg_std)

axs[2].set_title('Met Data')
axs[2].imshow(tair_met)

plt.show()
