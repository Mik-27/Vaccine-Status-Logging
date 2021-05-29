import datetime
import json
import requests
from get_centres import find_by_district

print(datetime.datetime.now().time())

def check_dose_availability(centres, age_group, dose_no):
    """
        Check whether doses are available for specific age group, first or second dose, etc
        age_group - 18 or 45
        dose_no - 1 or 2 (strictly single digit)
    """
    if len(centres['sessions']) > 0:
        for i in range(len(centres['sessions'])):
            print("Centre: {}".format(centres['sessions'][i]["name"]))
            # Check age group
            if centres['sessions'][i]['min_age_limit'] == age_group:
                # Check availability of doses for the specific dose
                if centres['sessions'][i][f'available_capacity_dose{dose_no}'] > 0:
                    now_time = datetime.datetime.now().time()
                    print(f"[{now_time.strftime('%H:%M:%S')}]: Slot available for dose-{dose_no} for age {age_group}")