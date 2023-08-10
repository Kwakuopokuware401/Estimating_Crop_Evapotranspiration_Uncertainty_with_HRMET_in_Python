# Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET_in_Python

![working_example_plot](https://github.com/Kwakuopokuware401/Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET_in_Python/assets/94206249/d0623e0e-686b-49cd-b71e-585682b972d2)


Author:  Kwaku Opoku-Ware (kwakuopokuware401@gmail.com)


## Description 
Translating the HRMET evapotranspiration model to Python and applying it over gridded crop fields to estimate spatial ET uncertainty resulting from weather input errors. Focuses on perturbing inputs like temperature and radiation based on sensor specs and propagating through the Penman-Monteith model via Monte Carlo simulation.

## HRMET Gridded Evapotranspiration Model
This code implements the HRMET evapotranspiration model over a synthetic gridded domain. It also includes an analysis of input uncertainty and propagation through the model output.

## Model overview
HRMET is a relatively simple point evapotranspiration model that uses a Penman-Monteith approach. It requires standard weather data and vegetation/soil properties.

The core model is implemented in Python based on a translation from the original MATLAB code.

## Running the model
The entry point is hrmet.py by setting-up input variables. It allows running the model and visualizing outputs.

The key steps are:

-Set up synthetic gridded input data

-Loop over grid cells, running HRMET at each point

-Generate map of ET estimates
![Gridded_ET](https://github.com/Kwakuopokuware401/Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET_in_Python/assets/94206249/21fd5728-9dfa-4e41-947c-dd5e2b91a400)

-Estimate uncertainty in input data (here surface temperature)

-Propagate uncertainty through to ET outputs

-Analyze uncertainty statistics

## Requirements
The code requires the following Python packages:

-numpy

-matplotlib

-datetime

## Applications
Potential use cases for this modeling approach include:

![Comparing Uncertainty techniques](https://github.com/Kwakuopokuware401/Estimating_Crop_Evapotranspiration_Uncertainty_with_HRMET_in_Python/assets/94206249/1abf2412-0440-469e-9ba1-77c7ca49d488)


-Spatial analysis of ET over agricultural fields

-ET forecasting for drought monitoring

-Hydrologic modeling of watersheds

-Quantifying uncertainty in hydrologic predictions

## References
The HRMET model, written in Matlab code, was originally developed by Sam Zipper (samzipper@ku.edu). If you utilize or adapt the HRMET model in your work, please cite the following paper to credit the original model developers:

    Zipper, S.C. & S.P. Loheide II (2014). Using evapotranspiration to
    assess drought sensitivity on a subfield scale with HRMET, a high
    resolution surface energy balance model. Agricultural & Forest
    Meteorology 197: 91-102. DOI: 10.1016/j.agrformet.2014.06.009

Link: http://dx.doi.org/10.1016/j.agrformet.2014.06.009

I appreciate you acknowledging the research contributions that enabled the development of HRMET. Citing relevant papers helps advance scientific progress through the open dissemination of knowledge. Please let me know if you have any questions about appropriately citing this model.
