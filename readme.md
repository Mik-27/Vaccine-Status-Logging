# Vaccinations Slots Check

- This small code was basically created to create a log of the vaccination centres and the availability in them.
- It is developed with the general idea of knowing when the vaccination booking on the Cowin starts and user can log in at that time.
- It uses the [Cowin API](https://apisetu.gov.in/public/marketplace/api/cowin) for fetching the data using the various Restful APIs provided.

## Getting Started

Better to have a virtual environment set for the files.

Installation: 
<code>pip install virtualenv</code>
<!-- ```sdgghhfh``` -->
Setting up Virtual Env: ```python3 -m venv /path/to/new/virtual/environment```

### Install the prerequisites using the requirements.txt file.

```pip install -r requirements.text```

## Setting Environment variables

Set the following variables in a file named ```.env``` in the this folder itself.

```STATE``` : Name of the state

```DIST_ID``` : Numerical id for the specific district; can be obtained by using ```get_district_id()``` funtion.

```BLOCK_NAME``` : Name of the block within the district selected.

## Running the application

- The ```get_centres.py``` file contains functions for retrieving the data regarding state, districts, etc.

- ```check_slots.py``` contains the function for making request to the API for vaccinations slots availability every 5 seconds approx. by providing it the location information.

- Run the code in the command prompt by moving to the folder location and execting the command:
```python check_slots.py```

## Logging
- After running the logs will be displayed in the command prompt containing information such as time, centre name and availability of vaccine.
- The logs will also be saved in the ```vac.log``` to refer in the future as to at what time did the vaccines bacame available.

## Future Prospects
- GUI application for the same for ease of entering environment variables.
- Alerts on availability of vaccine.

## Authors
- Mihir Thakur

## Acknowledgements
- Got the inspiration after reading a lot of articles regarding the use of API for booking slots.
- Frustrated due to non-availability of vaccines in my area.
- PS: Finally Vaccinated.