import matplotlib.pyplot as plt
import numpy as np

# Function to plot the 2D ET grid 
def plot_et_grid(et_grid, title='Evapotranspiration'):
  """Plot 2D map of ET grid"""

  # Create a new figure and axes object
  fig, ax = plt.subplots()

  # Plot the ET grid using pcolormesh, which handles discrete grids
  # Use a blue colormap to indicate low to high ET
  cax = ax.pcolormesh(et_grid, cmap='Blues')

  # Add a colorbar to show the ET scale
  fig.colorbar(cax) 

  # Add plot title and axis labels
  ax.set_title(title)
  ax.set_xlabel('Column index')
  ax.set_ylabel('Row index')

# Function to plot an uncertainty map
def plot_uncertainty(data, title='Uncertainty'):
  
  # Create figure and axes
  fig, ax = plt.subplots()

  # Plot uncertainty grid using pcolormesh
  # Use a red colormap to show low to high uncertainty
  cax = ax.pcolormesh(data, cmap='Reds')

  # Add colorbar
  fig.colorbar(cax)

  # Add title
  ax.set_title(title)

# Function to plot ensemble mean and standard deviation
def plot_ensemble(data_mean, data_std, title='Ensemble'):
  
  # Create figure with two axes for mean and stddev
  fig, axs = plt.subplots(1, 2, figsize=(10, 5))

  # Plot mean ET ensemble on left
  axs[0].pcolormesh(data_mean, cmap='Blues')
  axs[0].set_title('Mean')

  # Plot ET standard deviation on right
  axs[1].pcolormesh(data_std, cmap='Reds')
  axs[1].set_title('Standard Deviation')

  # Add overall title 
  fig.suptitle(title)
  
# Function to set global matplotlib plot style  
def set_plot_params():

  # Set default font size and title size
  plt.rcParams['font.size'] = 14
  plt.rcParams['axes.titlesize'] = 18
  
  # Use ggplot style for clean, readable plots
  plt.style.use('ggplot')
