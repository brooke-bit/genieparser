import csv
import requests
import json

# API endpoint URLs
devices_url = "https://api.mist.com/api/v1/sites/{site_id}/devices/{ap_id}"
assign_url = "https://api.mist.com/api/v1/deviceprofiles/{deviceprofile_id}/assign"

# Mist API credentials and site ID
token = "xxx"
site_id = "xxx"

# Read AP IDs, new names, and MAC addresses from CSV
ap_data = []
with open('b3_ap_data.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        ap_id = row['AP ID']
        new_name = row['New Name']
        mac_address = row['Mac']
        deviceprofile_id = row['Device Profile ID']
        ap_data.append({"ap_id": ap_id, "new_name": new_name, "mac_address": mac_address, "deviceprofile_id": deviceprofile_id})

# Update AP names and assign MAC addresses to device profiles
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token {}'.format(token)
}

for ap in ap_data:
    ap_id = ap['ap_id']
    new_name = ap['new_name']
    mac_address = ap['mac_address']
    deviceprofile_id = ap['deviceprofile_id']

    # Update AP name
    url = devices_url.format(site_id=site_id, ap_id=ap_id)
    payload = {
        "name": new_name
    }
    response = requests.put(url, headers=headers, json=payload)
    print(response.text)

    # Assign MAC address to device profile
    url = assign_url.format(deviceprofile_id=deviceprofile_id)
    payload = {
        "mac": mac_address
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)
