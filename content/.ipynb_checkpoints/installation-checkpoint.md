# Installation


### Setting up Python Environment
1. On the UMD cluster, first load the anaconda module and create a clone environment by typing the 
following commands on the terminal:<br>
`module load python/3.8/anaconda`<br>
`conda create -n UMD --clone=/apps/python/3.7/anaconda` <br><br>
On a non-UMD cluster or local machine, download and install the latest anaconda package <br>
`wget -c https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh` <br>
`bash Anaconda3-2022.05-Linux-x86_64.sh` <br>
`conda create --name UMD`
<br> 

```{note}
You can replace UMD with a different environment name of your choice
```
<br>

2. Next copy-paste the following commands into the terminal:<br>
`conda activate UMD`<br>
`conda install -c conda-forge logzero` <br>
`conda install -c conda-forge netcdf4` <br>
`conda install -c conda-forge gdal`<br>
`conda install -c conda-forge rasterio`<br>
`conda install -c conda-forge pyresample`<br>
`conda install -c conda-forge cdsapi`<br>
`conda install -c conda-forge geopandas`<br>
`conda install -c conda-forge seaborn`<br>
`conda install -c conda-forge xarray`<br>
`conda install -c conda-forge rasterstats`<br>
`conda install -c conda-forge tqdm`<br>
`conda install -c conda-forge scikit-learn`<br>
`conda install -c conda-forge jupyterlab`<br>
`conda install -c conda-forge catboost`<br>
`conda install -c conda-forge arrow`<br>
`conda install -c anaconda netcdf4`<br>
`conda install -c conda-forge cartopy`<br>
`pip install wget pyModis merf tsfresh pyshp palettable geopy geocoder palettable forestci pangres sklearn-contrib-lightning wget pangres pycountry matplotlib-scalebar`<br>
`pip install --upgrade git+https://github.com/ritviksahajpal/pygeoutil.git` <br>


### MODIS NDVI
1. Create an account on the [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) website
2. Follow the instructions [here](https://ladsweb.modaps.eosdis.nasa.gov/learn/download-files-using-laads-daac-tokens/) 
to request a token for your account.
   (i) Login by going to Profile -> Earthdata Login
 <br>
   <img src="../images/NDVI_Step2_img1.png" alt="profile" class="bg-primary" width="700px">
<br>


   (ii) Enter your login credentials or register  
   <img src="../images/NDVI_Step2_img2.png" alt="login" class="bg-primary" width="500px">
 <br>  
 
 
   (iii) Select Profile -> Generate Token from the top menu 
 <br>
    <img src="../images/NDVI_Step2_img3.png" alt="generate token" class="bg-primary" width="500px">
 <br>
 
 
   (iv)Copy the token from this window and store it somewhere safe and secure <img src="../images/NDVI_Step2_img4.png" alt="token" class="bg-primary" width="500px">
 <br>
 
3. On your local machine/cluster, iIf not already installed, 
install [octvi](https://pypi.org/project/octvi/)
<br>
4. On the command prompt type `octviconfig` and at the place it asks for a token, 
paste the token you copied earlier.

### AgERA5
1. Create an account on the [CDS](https://cds.climate.copernicus.eu) website 
2. Follow the instructions [here](https://cds.climate.copernicus.eu/api-how-to/)
to install the CDS API key on your local machine/cluster
3. Follow these instructions to install the CDS API Key on your local machine/cluster

     <b><u>A. For Windows users:</u></b> 
     <br>
  (i)Login to [CDS](https://cds.climate.copernicus.eu/user/143426/)      
        <img src="../images/AGRE5_Step2_CDSLogin.png" alt="CDSLogin" class="bg-primary" width="500px">
        
<br>        
  (ii)Copy a 2 line code, which shows a url and your own uid:API key details as followed:
        
   a. For CDS users, Go to [this](https://cds.climate.copernicus.eu/api-how-to/) page and copy the 2 line code                     displayed in the black box  as shown below:
<br>
    `url:https://cds.climate.copernicus.eu/api/v2`<br>`key: {uid}:{api-key}` 
<br>
         
              
   b. For ADS users, Go to [this](https://ads.atmosphere.copernicus.eu/api-how-to/)page and copy the 2 line code                   displayed in the black box in the "Install the CDS API key" section as shown below:
            `url:https://ads.atmosphere.copernicus.eu/api/v2` <br> `key: {uid}:{api-key}`
<br>              
  (iii)Paste the 2 line code into a  %USERPROFILE%\.cdsapirc file, where in your windows environment, %USERPROFILE% is             usually located at C:\Users\Username folder). The CDS API expects to find the .cdsapirc file in your home                   directory. 
<br>         
  (iv)Install the CDS API client by running the following command in a Command Prompt window:
         a. For python 2.7 
 <br>
         `pip install cdsapi`
<br>
          b.For Python 3
<br>
         `pip3 install cdsapi`
<br>        
                
  (v)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS and ADS             catalogues. It is necessary to agree to the Terms of Use of every datasets that you intend to download. Attached             to each dataset download form, the "Show API request" button displays the python code to be used.
    
<br>      
   <b><u>B. For Mac users:</u></b> 
   
   (i)Login to [CDS](https://cds.climate.copernicus.eu/user/143426/)
   
   <img src="../images/AGRE5_Step2_CDSLogin.png" alt="CDSLogin" class="bg-primary" width="700px">
        
<br>        
   (ii)Copy a 2 line code, which shows a url and your own uid:API key details as followed:
      
   a. For CDS users, Go to [this](https://cds.climate.copernicus.eu/api-how-to/) page and copy the 2 line code                     displayed in the black box as shown:<br>`url:https://cds.climate.copernicus.eu/api/v2`<br>`key: {uid}:{api-key}`
    <br> 
   b. For ADS users, Go to [this](https://ads.atmosphere.copernicus.eu/api-how-to/)page and copy the 2 line code                   displayed in the black box as shown:
 <br>
      `url:https://ads.atmosphere.copernicus.eu/api/v2` <br> `key: {uid}:{api-key}`
<br>         
   (iii)Create your key file in your home directory in your Terminal window as follows:<br>
            `touch ~/.cdsapirc`
<br>            
   (iv)Edit your key file and paste the two lines you copied in Step 2 above to your .cdsapirc key file.
<br>      
   (v)Install the CDS API client using pip, by running the following command in your Terminal window:
<br>
            `pip install cdsapi` <br>
            
   (vi)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS and ADS             catalogues. It is necessary to agree to the Terms of Use of every datasets that you intend to download. Attached             to each dataset download form, the "Show API request" button displays the python code to be used.
<br>
            
  <b><u>C. For Linux users:</u></b> 
<br>
    `Install the API Key`
<br>
   (i)If you don't have an account, please self register at the [CDS registration page](https://cds.climate.copernicus.eu/user/register?destination=%2F%23!%2Fhome/)
      
   (ii)If you are not logged, please [login](https://cds.climate.copernicus.eu/user/login?destination=%2F%23!%2Fhome) and           go to the step below.
      
   (iii)Copy the code displayed into HOME/.cdsapirc file (in your Unix/Linux environment).<br>
      `url:https://cds.climate.copernicus.eu/api/v2` <br>`key: {uid}:{api-key}`
<br>                      
   <b>Install the API Client</b><br>
   
   (i)The CDS API client is a python based library. It provides support for both Python 2.7.x and Python 3.You can                Install the CDS API client via the package management system pip, by running on Unix/Linux the command shown in the          box beside <br>
         `pip install cdsapi`   
<br>        
   <b>Use the CDS API client for data access</b><br>
   
   (i)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS catalogue.          It is necessary to agree to the Terms of Use of every datasets that you intend to download.
<br> 
   (ii)Attached to each dataset download form, the following button[show API Request]displays the python code to be used.           The request can be formatted using the interactive form. The api call must follow the syntax:
<br>
    `import cdsapi`<br>`c = cdsapi.Client()`<br>`c.retrieve("dataset-short-name", {... sub-selection request ...},"target-file")` <br>
    
  (iii)If not already installed, install the `cdsapi` python library by typing `pip install cdsapi` in 
the command prompt.
