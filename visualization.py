import matplotlib.pyplot as plt
import numpy as np

def plot_et_grid(et_grid, title='Evapotranspiration'):
    """Plot 2D map of ET grid"""
    
    fig, ax = plt.subplots()
    cax = ax.pcolormesh(et_grid, cmap='Blues')
    fig.colorbar(cax)
    ax.set_title(title)
    ax.set_xlabel('Column index')
    ax.set_ylabel('Row index')

def plot_uncertainty(data, title='Uncertainty'):
    """Plot uncertainty map"""
    
    fig, ax = plt.subplots()
    cax = ax.pcolormesh(data, cmap='Reds')
    fig.colorbar(cax)
    ax.set_title(title)
    
def plot_ensemble(data_mean, data_std, title='Ensemble'):
    """Plot mean and std deviation of ensemble"""
    
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    axs[0].pcolormesh(data_mean, cmap='Blues')
    axs[0].set_title('Mean')
    
    axs[1].pcolormesh(data_std, cmap='Reds') 
    axs[1].set_title('Standard Deviation')
    
    fig.suptitle(title)

def set_plot_params():
    """Set matplotlib plot parameters"""

    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.titlesize'] = 18
    
    plt.style.use('ggplot')
