import requests as re
import json
import time
from datetime import date
from rich.table import Table


centers = [
      # Jamnagar Corporation
      {
            'district_id' : 773,
            'date' : date.today().strftime("%d-%m-%Y")
      },

      # Jamnagar
      {
            'district_id' : 169,
            'date' : date.today().strftime("%d-%m-%Y"),
      }
]

headers  ={
      "accept": "application/json",
      "Accept-Language": "hi_IN",
}

def find_active(block, data, age=18):
      # data = []
      sessions = block['sessions']
      for sess in sessions:
            if sess["min_age_limit"] == age and sess["available_capacity"] > 0:
                  # T.add_row(block["name"], str(sess["available_capacity"]), str(sess["date"]), block["block_name"])
                  data.append([block["name"], str(sess["available_capacity"]), str(sess["date"]), block["block_name"]])

def get_data(centers, age, req_table = False):
      
      data = []

      for center in centers:
            
            req = re.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict", headers=headers, params=center)
            req = req.json()
            
            for block in req["centers"]:
                  if block["block_name"] == "Jamnagar" or block["block_name"] == "Jamnagar Corporation": 
                        find_active(block, data, age=age)

      if req_table:
            table = Table(title= f"Available Slots for Vaccination for age {age}")
            table.add_column("Center Name", justify="center", style="cyan", no_wrap=True)
            table.add_column("Available Doses", justify="center", style="blue", no_wrap=True)
            table.add_column("Date", justify="center", style="green", no_wrap=True)
            table.add_column("Block Name", justify="center", style="magenta", no_wrap=True)

            for D in data:
                  table.add_row(*D)
            
            return table

      return data