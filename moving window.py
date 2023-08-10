import numpy as np

# Function to calculate moving window mean and standard deviation
# for a 2D input array
def moving_window(in_array, window):

  # Window size must be odd integer
  assert window % 2 != 0  

  # Calculate center index of window
  shift = (window - 1) // 2  

  # Output arrays to store results
  out_mean = np.full_like(in_array, np.nan)
  out_std = np.full_like(in_array, np.nan)

  # Loop over interior indices skipping edges
  for i in range(shift, in_array.shape[0] - shift):   
    for j in range(shift, in_array.shape[1] - shift):
      
      # Extract window values centered on current index
      window_vals = in_array[i-shift:i+shift+1, j-shift:j+shift+1]  

      # Calculate mean and standard deviation in window
      out_mean[i,j] = np.mean(window_vals)
      out_std[i,j] = np.std(window_vals)

  # Return output arrays
  return out_mean, out_std
