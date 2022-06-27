# Downloading and Processing EO Data

A Python package to prepare (download, extract, process input data) for GEOCIF and related models

## Installation

`pip install --upgrade --no-deps --force-reinstall git+https://github.com/ritviksahajpal/geoprepare.git`

## Usage
`import geoprepare.geoprepare as gprp`<br>
`gprp.run(PATH_TO_CONFIG_FILE)`

## Configuration File

`[DATASETS]<br>
datasets = ['CHIRPS']<br>
dir_base = <br>

[DEFAULT]<br>
logfile = log<br>
parallel_process = True<br>
fraction_cpus = 0.5<br>
start_year = 1982<br>
end_year = 2022`<br>

