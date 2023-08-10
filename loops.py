# Loop and run HRMET
for i in range(nrow):
  for j in range(ncol):

    lai = LAI_grid[i,j]
    height = h_grid[i,j]
    temp = T_grid[i,j]

    ET_grid[i,j] = hrmet(datetime[i,j], longitude[i,j], latitude[i,j],  
                         Tair[i,j], SWin[i,j], u[i,j], ea[i,j], pa[i,j],
                         lai, height, temp, albSoil[i,j], albVeg[i,j],
                         emissSoil[i,j], emissVeg[i,j])
