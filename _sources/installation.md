# Installation


### Setting up Python Environment
1. On the UMD cluster, first load the anaconda module and create a clone environment by typing the 
following commands on the terminal:<br>
`module load python/3.8/anaconda`<br>
`conda create -n UMD --clone=/apps/python/3.8/anaconda` <br><br>
On a non-UMD cluster or local machine, download and install the latest anaconda package
`wget -c https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh` <br>
`bash Anaconda3-2022.05-Linux-x86_64.sh`
<br><br>
2. Next copy-paste the following commands into the terminal:<br>
`conda init bash`<br>
`conda activate UMD`<br>
`conda update anaconda`<br>
`conda install gdal`<br>
`conda install rasterio`<br>
`conda install numpy`<br>
`conda install pandas`<br>
`conda install geopandas`<br>
`conda install scikit-learn`<br>
`conda install jupyterlab`<br>
`conda install matplotlib`<br>
`conda install seaborn`<br>
`conda install xarray`<br>
`conda install rasterstats`<br>
`conda install tqdm`<br>
`conda install pytest`<br>
`conda install sqlalchemy`<br>
`conda install scikit-image`<br>
`conda install scipy`<br>
`conda install pysal`<br>
`conda install beautifulsoup4`<br>
`conda install boto3`<br>
`conda install cython`<br>
`conda install statsmodels`<br>
`conda install future`<br>
`conda install graphviz`<br>
`conda install pylint`<br>
`conda install mlxtend`<br>
`conda install line_profiler`<br>
`conda install nodejs`<br>
`conda install sphinx`<br>
`conda install nbsphinx`<br>
`conda install catboost`<br>
`conda install arrow`<br>
`conda install contextily`<br>
`conda install openpyxl`<br>
`conda install -c conda-forge eemont`<br>
`conda install -c conda-forge logzero`<br>
`conda install -c conda-forge tinydb`<br>
`conda install -c anaconda netcdf4`<br>
`conda install -c conda-forge cachetools`<br>
`conda install -c conda-forge pygeoprocessing`<br>
`conda install -c conda-forge pygmt`<br>
`conda install -c conda-forge dataset`<br>
`conda install -c conda-forge pyresample`<br>
`conda install -c conda-forge cartopy`<br>
`conda install -c conda-forge eli5`<br>
`conda install -c conda-forge lime`<br>
`conda install -c conda-forge skrebate`<br>
`conda install -c conda-forge neptune-client`<br>
`conda install -c conda-forge xgboost`<br>
`conda install -c conda-forge pandas-profiling`<br>
`conda install -c conda-forge bottleneck`<br>
`conda install -c conda-forge chardet`<br>
`conda install -c conda-forge sentinelhub`<br>
`conda install -c conda-forge pygam`<br>
`conda install -c conda-forge watchdog`<br>
`conda install -c conda-forge retrying`<br>
`conda install -c conda-forge fiona`<br>
`conda install -c conda-forge tpot`<br>
`conda install -c conda-forge cdsapi`<br>
`conda install -c conda-forge scikit-garden`<br>
`conda install -c conda-forge neptune-client`<br>
`conda install -c conda-forge urllib3`<br>
`conda install -c ncar pynio`<br>
`conda install -c conda-forge mpi4py`<br>
`conda install -c conda-forge scikit-optimize`<br>
`conda install -c conda-forge requests`<br>
`pip install --upgrade git+https://github.com/ritviksahajpal/pygeoutil.git`   
`pip install merf tsfresh pyshp palettable geopy geocoder palettable forestci pangres sklearn-contrib-lightning wget pangres pycountry matplotlib-scalebar`<br>
`pip install git+https://github.com/GeoscienceAustralia/uncover-ml.git`

### MODIS NDVI
1. Create an account on the [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) website
2. Follow the instructions [here](https://ladsweb.modaps.eosdis.nasa.gov/learn/download-files-using-laads-daac-tokens/) 
to request a token for your account.
   * Login by going to Profile -> Earthdata Login
   * Select Profile -> Generate Token from the top menu
   * Copy the token from this window and store it somewhere safe and secure
3. On your local machine/cluster, iIf not already installed, 
install octvi: https://pypi.org/project/octvi/
4. On the command prompt type `octviconfig` and at the place it asks for a token, 
paste the token you copied earlier.

### AgERA5
1. Create an account on the [CDS](https://cds.climate.copernicus.eu) website 
2. Follow the instructions [here](https://cds.climate.copernicus.eu/cds-client-web/user-guide/tokens/)
to install the CDS API key on your local machine/cluster
3. If not already installed, install the `cdsapi` python library by typing `pip install cdsapi` in 
the command prompt.