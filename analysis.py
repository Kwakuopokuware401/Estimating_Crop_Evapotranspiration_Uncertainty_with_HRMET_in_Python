import numpy as np

# Function to estimate T uncertainty using a moving window technique
def moving_window(data, n, std_only=True):

# Initialize empty lists to store mean and std dev for each window
means = []  
stds = []

# Loop through each row and column  
for i in range(nrow):
  for j in range(ncol):
   
    # Extract n x n window around current index
    # Use max/min to ensure we don't go out of bounds
    window = data[max(i-n,0):min(i+n,nrow), max(j-n,0):min(j+n,ncol)]

    # Calculate mean and standard deviation of values in window
    means.append(np.mean(window))  
    stds.append(np.std(window))

# Reshape the 1D list of stds to 2D array matched to input shape
if std_only:
  return np.reshape(stds, (nrow, ncol)) 

# Alternatively return tuples of means and stds
else:
  return means, stds
