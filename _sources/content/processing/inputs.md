# Processing Inputs 

```python
from geoprepare import geoprepare, geoextract

# Provide full path to the configuration files
# Download and preprocess data
geoprepare.run(['PATH_TO_geoprepare.txt', 'PATH_TO_geoextract.txt'])

# Extract crop masks and EO variables
geoextract.run(['PATH_TO_geoprepare.txt', 'PATH_TO_geoextract.txt'])
```

## Config files
### geoprepare.txt
1. Path where to store the downloaded and processed files: `dir_base`
2. Specify which datasets need to be downloaded and processed: `datasets`
3. Specify time-period for which data should be downloaded and processed: `start_year`, `end_year`
4. What fraction of available CPUs to use: `fraction_cpus`
5. What directory name to use for the log files: `logfile`
6. Whether to use multiple CPUs: `parallel_process`


### geoextract.txt
1. List of countries to process: `countries`
2. List of seasons to process: `forecast_seasons`