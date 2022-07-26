# Processing Inputs 

```python
from geoprepare import geoprepare, geoextract

# Provide full path to the configuration files
# Download and preprocess data
geoprepare.run(['PATH_TO_geoprepare.txt'])

# Extract crop masks and EO variables
geoextract.run(['PATH_TO_geoprepare.txt', 'PATH_TO_geoextract.txt'])
```

## Config files
### geoprepare.txt
`dir_base`: Path where to store the downloaded and processed files  
`datasets`: Specify which datasets need to be downloaded and processed   
`start_year`, `end_year`: Specify time-period for which data should be downloaded and processed  
`logfile`: What directory name to use for the log files  
`parallel_process`: Whether to use multiple CPUs  
`fraction_cpus`: What fraction of available CPUs to use  

### geoextract.txt
`countries`: List of countries to process  
`forecast_seasons`: List of seasons to process