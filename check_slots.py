import datetime
import time
import json
import requests
import logging
import os
from dotenv import load_dotenv

from get_centres import find_by_district

load_dotenv()

# Config for logging messages
logging.basicConfig(level=logging.INFO, 
                    format="[%(asctime)s] - %(message)s", 
                    datefmt="%d-%m-%Y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("vac.log"),
                        logging.StreamHandler()
                    ]
                )

today = datetime.datetime.now().strftime("%d-%m-%Y")

def check_dose_availability(centres, age_group, dose_no):
    """
        Check whether doses are available for specific age group, first or second dose, etc
        age_group - 18 or 45
        dose_no - 1 or 2 (strictly single digit)
    """
    now_time = datetime.datetime.now().time()
    if len(centres['sessions']) > 0:
        # print(centres['sessions'])
        for i in range(len(centres['sessions'])):
            logging.info("Centre: %s", centres['sessions'][i]["name"])
            # Check age group
            if centres['sessions'][i]['min_age_limit'] == age_group:
                # Check availability of doses for the specific dose
                if centres['sessions'][i][f'available_capacity_dose{dose_no}'] > 0:
                    logging.info("%s dose(s) available for %s+.\n ", centres['sessions'][i][f'available_capacity_dose{dose_no}'], age_group)
                else:
                    logging.info("Dose %s not available.\n", dose_no)
            else:
                logging.info("No centres available for age group %s.\n", age_group)
    else:
        logging.info("No vaccination centres available.\n")

# print(datetime.datetime.now().strftime("%d-%m-%Y"))
try:
    while True:
        check_dose_availability(find_by_district(os.environ.get("DIST_ID"), today, os.environ.get("BLOCK_NAME")), 45, 1)
        # Break the loop and end the program if time is 9 AM.
        if datetime.datetime.now().time().strftime("%H") == "09":
            break
        # Create a time interval of the specified time.
        time.sleep(5)
except KeyboardInterrupt:
    logging.error("Keyboard Interrupt.")
finally:
    logging.info("Logging Completed.")
