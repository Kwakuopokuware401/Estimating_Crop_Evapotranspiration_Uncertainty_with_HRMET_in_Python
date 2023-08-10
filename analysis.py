import numpy as np

# Function to estimate T uncertainty
def moving_window(data, n, std_only=True):

  means = []
  stds = []

  for i in range(nrow):
    for j in range(ncol):
    
      window = data[max(i-n,0):min(i+n,nrow), max(j-n,0):min(j+n,ncol)]
      means.append(np.mean(window))
      stds.append(np.std(window))

  if std_only:  
    return np.reshape(stds, (nrow, ncol))
  else:
    return means, stds
