import numpy as np

def hrmet(datetime, longitude, latitude, Tair, SWin, u, ea, pa, LAI, h, T, albSoil, albVeg, emissSoil, emissVeg):

  Rns = (1 - albSoil) * SWin + emissSoil * 5.67e-8 * (T**4 - Tair**4)

  G = 0.1 * Rns

  Rnl = emissVeg * 5.67e-8 * (T**4 - Tair**4)
  Ra_s = 0.2 * (Rns - G)

  LvE = 0.1 * LAI * (Rnl - Ra_s)

  ET_mmHr = LvE * 3600 / (1000 * 2.45)

  return ET_mmHr
