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
   <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\NDVI_Step2_img1.png" alt="profile" class="bg-primary" width="700px">
   
   * Enter your login credentials or register  
   <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\NDVI_Step2_img2.png" alt="login" class="bg-primary" width="500px">
   
   * Select Profile -> Generate Token from the top menu <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\NDVI_Step2_img3.png" alt="generate token" class="bg-primary" width="500px">
   
   * Copy the token from this window and store it somewhere safe and secure <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\NDVI_Step2_img4.png" alt="token" class="bg-primary" width="500px">
3. On your local machine/cluster, iIf not already installed, 
install octvi: https://pypi.org/project/octvi/
4. On the command prompt type `octviconfig` and at the place it asks for a token, 
paste the token you copied earlier.

### AgERA5
1. Create an account on the [CDS](https://cds.climate.copernicus.eu) website 
2. Follow the instructions [here](https://cds.climate.copernicus.eu/api-how-to/)
to install the CDS API key on your local machine/cluster
3. Follow these instructions to install the CDS API Key on your local machine/cluster
    # 1. For Windows users: 
    
      (i)Login to [CDS](https://cds.climate.copernicus.eu/user/143426/)      
        <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_CDSLogin.png" alt="CDSLogin" class="bg-primary" width="500px">
        
      (ii)Copy a 2 line code, which shows a url and your own uid:API key details as followed:
        
      A.For CDS users, Go to [this](https://cds.climate.copernicus.eu/api-how-to/) page and copy the 2 line code                     displayed in the black box in the "Install the CDS API key" section as shown below:      
      <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_CDSAPIUrl.png" alt="CDSurl" class="bg-primary" width="700px">
              
      B.For ADS users, Go to [this](https://ads.atmosphere.copernicus.eu/api-how-to/)page and copy the 2 line code                   displayed in the black box in the "Install the CDS API key" section as shown below:      
      <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_ADSAPIUrl.png" alt="ADSurl" class="bg-primary" width="700px">
              
      (iii)Paste the 2 line code into a  %USERPROFILE%\.cdsapirc file, where in your windows environment, %USERPROFILE% is             usually located at C:\Users\Username folder). The CDS API expects to find the .cdsapirc file in your home                   directory.
         
      (iv)Install the CDS API client by running the following command in a Command Prompt window:
                a. pip install cdsapi # for Python 2.7<br>
                b. pip3 install cdsapi # for Python 3  
        <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_installcdsapi.png" alt="installcds" class="bg-primary" width="500px">
                
      (v)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS and ADS             catalogues. It is necessary to agree to the Terms of Use of every datasets that you intend to download. Attached             to each dataset download form, the "Show API request" button displays the python code to be used.
      
   # 2. For Mac users: 
       
      (i)Login to [CDS](https://cds.climate.copernicus.eu/user/143426/)
        <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_CDSLogin.png" alt="CDSLogin" class="bg-primary" width="700px">
        
      (ii)Copy a 2 line code, which shows a url and your own uid:API key details as followed:
        
      A.For CDS users, Go to [this](https://cds.climate.copernicus.eu/api-how-to/) page and copy the 2 line code                     displayed in the black box in the "Install the CDS API key" section as shown below:<img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_CDSAPIUrl.png" alt="CDSurl" class="bg-primary" width="700px">
              
      B.For ADS users, Go to [this](https://ads.atmosphere.copernicus.eu/api-how-to/)page and copy the 2 line code                   displayed in the black box in the "Install the CDS API key" section as shown below:<img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_ADSAPIUrl.png" alt="ADSurl" class="bg-primary" width="700px">
      
      (iii)Create your key file in your home directory in your Terminal window as follows:
            <b><i>touch ~/.cdsapirc</i></b>
            
      (iv)Edit your key file and paste the two lines you copied in Step 2 above to your .cdsapirc key file.
      
      (v)Install the CDS API client using pip, by running the following command in your Terminal window:
            <b><i>pip install cdsapi</i></b>
            
      (vi)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS and ADS             catalogues. It is necessary to agree to the Terms of Use of every datasets that you intend to download. Attached             to each dataset download form, the "Show API request" button displays the python code to be used.
            
   # 3. For Linux users: 
      
     <b>Install the API Key</b>
     
      (i)If you don't have an account, please self register at the [CDS registration page](https://cds.climate.copernicus.eu/user/register?destination=%2F%23!%2Fhome/)
      
      (ii)If you are not logged, please [login](https://cds.climate.copernicus.eu/user/login?destination=%2F%23!%2Fhome) and           go to the step below.
      
      (iii)Copy the code displayed into HOME/.cdsapirc file (in your Unix/Linux environment).<img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_LinuxAPIKeyUrl.png" alt="ADSurl" class="bg-primary" width="700px">
                
   <b>Install the API Client</b>
   
      (i)The CDS API client is a python based library. It provides support for both Python 2.7.x and Python 3.You can                Install the CDS API client via the package management system pip, by running on Unix/Linux the command shown in the          box beside <img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_LinuxAPIClient.png" alt="ADSurl" class="bg-primary" width="700px">
      
   <b>Use the CDS API client for data access</b>
   
    (i)Once the CDS API client is installed, it can be used to request data from the datasets listed in the CDS catalogue.          It is necessary to agree to the Terms of Use of every datasets that you intend to download.
    
    (ii)Attached to each dataset download form, the following button[show API Request]displays the python code to be used.           The request can be formatted using the interactive form. The api call must follow the syntax:<img src="C:\Users\ishaa\Desktop\Tanzania_Rice\yield_forecasting\images\AGRE5_Step2_APICallSyntax.png" alt="ADSurl" class="bg-primary" width="700px">

3. If not already installed, install the `cdsapi` python library by typing `pip install cdsapi` in 
the command prompt.