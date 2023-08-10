import numpy as np

# HRMET model to calculate evapotranspiration 
def hrmet(datetime, longitude, latitude, Tair, SWin, u, ea, pa, LAI, h, T, albSoil, albVeg, emissSoil, emissVeg):

# Net shortwave radiation 
# Incoming shortwave * (1 - albedo)
Rns = (1 - albSoil) * SWin  

# Outgoing longwave radiation
# Emissivity * Stefan-Boltzmann * (Temp**4 - AirTemp**4) 
+ emissSoil * 5.67e-8 * (T**4 - Tair**4)

# Estimate soil heat flux as fraction of Rns
G = 0.1 * Rns  

# Net longwave radiation
# Emissivity * Stefan-Boltzmann * (Temp**4 - AirTemp**4)
Rnl = emissVeg * 5.67e-8 * (T**4 - Tair**4)  

# Aerodynamic resistance term 
Ra_s = 0.2 * (Rns - G)  

# Latent heat flux 
# Function of LAI and radiation terms
LvE = 0.1 * LAI * (Rnl - Ra_s)  

# Convert latent heat flux to ET in mm/hour
ET_mmHr = LvE * 3600 / (1000 * 2.45)

return ET_mmHr
