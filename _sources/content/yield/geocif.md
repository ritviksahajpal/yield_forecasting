# GEOCIF

## Python code 
We will be using the [geocif](https://github.com/ritviksahajpal/geocif) package.
Before running any code, consider using `tmux` or `screen` to retain access to the terminal even if you are accidentally logged out.
```python
from geocif import geocif

# Provide full path to the configuration files
# Merge EO files into one, this is needed to create AgMet graphics and to run the crop yield model
geocif.run(['PATH_TO_geoprepare.txt', 'PATH_TO_geoextract.txt', 'PATH_TO_geocif.txt'])
```