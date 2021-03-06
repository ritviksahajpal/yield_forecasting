# Processing Inputs 

In this section, we will explore the steps required to download and process the input data needed for running a crop yield model or generating AgMet 
graphics.

## Background Information
We will be using Python configuration files to separate our code and user configurable settings.
Here is a [tutorial](https://docs.python.org/3/library/configparser.html) on how Python handles configuration files.

## Python code 
The code used to download and process the input data and then extract crop masks and EO variables is as follows:

```python
from geoprepare import geoprepare, geoextract

# Provide full path to the configuration files
# Download and preprocess data
geoprepare.run(['PATH_TO_geoprepare.txt'])

# Extract crop masks and EO variables
geoextract.run(['PATH_TO_geoprepare.txt', 'PATH_TO_geoextract.txt'])
```

Before running the code above, we need to specify the two configuration files. `geoprepare.txt` contains configuration settings for downloading and processing the input data. 
`geoextract.txt` contains configuration settings for extracting crop masks and EO variables.

## Configuration files
### geoprepare.txt
```python
[DATASETS]
datasets = ['CPC', 'SOIL-MOISTURE', 'LST', 'CPC', 'AVHRR', 'AGERA5', 'CHIRPS', 'CHIRPS-GEFS']

[PATHS]
dir_base = D:\
dir_input = ${dir_base}/input
dir_log = ${dir_input}/log
dir_interim = ${dir_input}/interim
dir_download = ${dir_input}/download
dir_output = ${dir_base}/output
dir_global_datasets = ${dir_input}/global_datasets

[AGERA5]
start_year = 2022

[AVHRR]
data_dir = https://www.ncei.noaa.gov/data/avhrr-land-normalized-difference-vegetation-index/access

[CHIRPS]
fill_value = -2147483648
prelim = /pub/org/chc/products/CHIRPS-2.0/prelim/global_daily/tifs/p05/
final = /pub/org/chc/products/CHIRPS-2.0/global_daily/tifs/p05/
start_year = 2022

[CHIRPS-GEFS]
fill_value = -2147483648
data_dir = /pub/org/chc/products/EWX/data/forecasts/CHIRPS-GEFS_precip_v12/15day/precip_mean/

[CPC]
data_dir = ftp://ftp.cdc.noaa.gov/Datasets

[ESI]
data_dir = https://gis1.servirglobal.net//data//esi//

[FLDAS]

[LST]
num_update_days = 7

[NDVI]
product = MOD09CMG
vi = ndvi
scale_glam = False
scale_mark = True
print_missing = False

[SOIL-MOISTURE]
data_dir = https://gimms.gsfc.nasa.gov/SMOS/SMAP/L03/

[LOGGING]
level = ERROR

[DEFAULT]
logfile = log
parallel_process = False
fraction_cpus = 0.5
start_year = 2022
end_year = 2022
```
`datasets`: Specify which datasets need to be downloaded and processed   
`dir_base`: Path where to store the downloaded and processed files  
`start_year`, `end_year`: Specify time-period for which data should be downloaded and processed  
`logfile`: What directory name to use for the log files  
`level`: Which level to use for logging (https://www.loggly.com/ultimate-guide/python-logging-basics/)    
`parallel_process`: Whether to use multiple CPUs  
`fraction_cpus`: What fraction of available CPUs to use  

### geoextract.txt
```python
[kenya]
category = EWCM
calendar_file = EWCM_2021-6-17.xlsx
shp_boundary = EWCM_Level_1.shp
crops = ['mz', 'sr', 'ml', 'rc', 'ww', 'tf']
use_cropland_mask = True

[ww]
mask = cropland_v9.tif

[mz]
mask = cropland_v9.tif

[sb]
mask = cropland_v9.tif

[rc]
mask = cropland_v9.tif

[tf]
mask = cropland_v9.tif

[sr]
mask = cropland_v9.tif

[ml]
mask = cropland_v9.tif

[DEFAULT]
redo = False
threshold = True
floor = 20
ceil = 90
countries = ['kenya']
forecast_seasons = [2022]
mask = cropland_v9.tif
eo_model = ['ndvi', 'cpc_tmax', 'cpc_tmin', 'cpc_precip', 'esi_4wk', 'soil_moisture_as1', 'soil_moisture_as2']
```
`countries`: List of countries to process  
`forecast_seasons`: List of seasons to process  
`mask`: Name of file to use as a mask for cropland/croptype  
`redo`: Whether to redo the processing for all days rather than process only days for which we have new data  
`threshold`: Whether to use a `threshold` value (`floor`) or a `percentile` (`ceil`) on the cropland/croptype mask  
`floor`: Value below which to set the mask to 0  
`ceil`: Value above which to set the mask to 1  
`eo_model`: List of datasets to extract from  


