# Loop over each grid cell index i (row), j (column)
for i in range(nrow):
  for j in range(ncol):

    # Extract scalar input values for this grid cell from the 
    # predefined input arrays:
    
    # LAI, canopy height, and surface temperature come from 
    # the randomly generated gridded arrays
    lai = LAI_grid[i,j]  
    height = h_grid[i,j]
    temp = T_grid[i,j]  

    # Air temperature, incoming solar radiation, wind speed, vapor pressure,
    # and surface pressure come from the constant value arrays defined
    # for the entire domain
    tair = Tair[i,j]   
    swin = SWin[i,j]
    wind = u[i,j]
    vapor = ea[i,j]  
    pressure = pa[i,j]

    # Longitude, latitude, and timestamp come from the constant value 
    # arrays defined for the entire domain
    lon = longitude[i,j]
    lat = latitude[i,j]
    dt = datetime[i,j]

    # Canopy radiative properties like albedo and emissivity come
    # from the constant value arrays defined for the domain
    alb_veg = albVeg[i,j]
    emiss_veg = emissVeg[i,j]

    # Call the HRMET function, passing the scalar inputs for this
    # grid cell. HRMET calculates the evapotranspiration rate for
    # a single point.
    ET_grid[i,j] = hrmet(dt, lon, lat, tair, swin, wind, vapor, pressure,
                         lai, height, temp, albSoil[i,j], albVeg[i,j],  
                         emissSoil[i,j], emissVeg[i,j])

    # Store the resulting ET value for this grid cell in the 
    # ET_grid array
