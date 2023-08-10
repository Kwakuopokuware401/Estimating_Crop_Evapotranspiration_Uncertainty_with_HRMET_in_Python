# Inputs
nrow, ncol = 50, 50

longitude = -89.4 * np.ones((nrow, ncol))  
latitude = 43.1 * np.ones((nrow, ncol))

datetime = np.full((nrow, ncol), datetime.datetime(2020, 6, 15, 12))

Tair = 25 * np.ones((nrow, ncol))
SWin = 500 * np.ones((nrow, ncol))
u = 2 * np.ones((nrow, ncol)) 
ea = 2.5 * np.ones((nrow, ncol))
pa = 101 * np.ones((nrow, ncol))

LAI_grid = np.random.rand(nrow, ncol) * 6
h_grid = np.random.rand(nrow, ncol) * 2
T_grid = np.random.rand(nrow, ncol) * 10 + 285

albSoil = 0.25 * np.ones((nrow, ncol))
albVeg = 0.2 * np.ones((nrow, ncol))  
emissSoil = 0.95 * np.ones((nrow, ncol))
emissVeg = 0.97 * np.ones((nrow, ncol))
