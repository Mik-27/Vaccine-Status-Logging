import datetime
import time
import json
import requests
import logging
from get_centres import find_by_district

# Config for logging messages
logging.basicConfig(level=logging.INFO, 
                    format="[%(asctime)s] - %(message)s", 
                    datefmt="%d-%m-%Y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("vac.log"),
                        logging.StreamHandler()
                    ]
                )

def check_dose_availability(centres, age_group, dose_no):
    """
        Check whether doses are available for specific age group, first or second dose, etc
        age_group - 18 or 45
        dose_no - 1 or 2 (strictly single digit)
    """
    now_time = datetime.datetime.now().time()
    if len(centres['sessions']) > 0:
        for i in range(len(centres['sessions'])):
            logging.info("Centre: %s", centres['sessions'][i]["name"])
            # Check age group
            if centres['sessions'][i]['min_age_limit'] == age_group:
                # Check availability of doses for the specific dose
                if centres['sessions'][i][f'available_capacity_dose{dose_no}'] > 0:
                    logging.info("Slot available for dose-%s for age %s.\n", dose_no, age_group)
                else:
                    logging.info("Dose %s not available.\n", dose_no)
            else:
                logging.info("No centres available for age group %s.\n", age_group)
    else:
        logging.info("No vaccination centres available.\n")

try:
    while True:
        check_dose_availability(find_by_district("394", "29-05-2021", "VVCMC"), 45, 1)
        # Break the loop and end the program if time is 9 AM.
        if datetime.datetime.now().time().strftime("%H") == "09":
            break
        # Create a time interval of the specified time.
        time.sleep(5)
except KeyboardInterrupt:
    logging.error("Keyboard Interrupt.")
finally:
    logging.info("Logging Completed.")
