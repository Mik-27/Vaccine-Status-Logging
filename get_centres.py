import datetime
import json
import requests

browser_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'}

def get_state_id(state="Maharashtra"):
    """
        Getting the state id from the complete list of states for the specified state
    """
    states_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    res = requests.get(states_url, headers=browser_header)
    states = json.loads(res.text)

    for i in range(len(states['states'])):
        if states['states'][i]['state_name'] == state:
            return states['states'][i]['state_id']


def get_distrcit_id(state_id, district):
    """
        Getting the specifie district from the specified state through state_id
    """
    dist_url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}"
    res = requests.get(dist_url, headers=browser_header)
    districts = json.loads(res.text)

    for i in range(len(districts['districts'])):
        if districts['districts'][i]['district_name'] == district:
            return districts['districts'][i]['district_id']


def find_by_district(dist_id, date, block):
    """
        Find the vaccination centres in a specific area and doses available using District ID and the Date.
    """
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={dist_id}&date={date}"
    res = requests.get(url, headers=browser_header)
    vac_centres = json.loads(res.text)

    # Storing centres od specific area/block in a differnt dictionary
    centres = {
        "sessions":[]
    }
    for i in range(len(vac_centres['sessions'])):
        if vac_centres['sessions'][i]['block_name'] == block:
            centres["sessions"].append(vac_centres['sessions'][i])

    return centres
