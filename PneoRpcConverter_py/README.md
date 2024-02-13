# PNEO to PHR metadata Converter
Converts the PNEO RPC xml metadata file to match with PHR RPC xml metadata syntax.

## Installation of dependencies
We recommend to create a virtual environment. 
Use following commands to create a virtual environment and activate it.
```
python3 -m venv venv_converter
source venv_converter/bin/activate
```
To install the dependencies, run:
```
pip install -r requirements.txt
```

## Running tests
Install the test dependencies by running:
```
pip install -r requirements-test.txt
```
To run the tests, run:
```
python3 -m pytest
```

## Usage
Run the script `pneo_to_phr.py`.
Please update the following variables before running the script:
 - pneo_xml_path: Path to the source PNEO RPC xml file
 - out_dir: Path to the directory where the converted xml file will be generated. The script will create the folder by itself.

## Support
Should you need any help, please reach out to any/all of the following:
 - `support@up42.com`: UP42 Customer Success Team
 - `pelle-svante.john@up42.com`: Pelle Svante John, Senior Product Manager, Analytics, UP42
 - `naman.jain@up42.com`: Naman Jain, Data Science Engineer, Analytics, UP42