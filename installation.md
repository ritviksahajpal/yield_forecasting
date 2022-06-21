# Installation

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