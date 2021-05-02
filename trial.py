from plyer import notification, Sms


notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
    timeout=10,  # seconds
)


# jam_corp = {
#       'district_id' : 773,
#       'date' : date.today().strftime("%d-%m-%Y")
# }

# jam = {
#       'district_id' : 169,
#       'date' : date.today().strftime("%d-%m-%Y"),
# }

# headers  ={
#       "accept": "application/json",
#       "Accept-Language": "hi_IN",
# }

# table = Table(title="Available Slots for Vaccination")
# table.add_column("Center Name", justify="center", style="cyan", no_wrap=True)
# table.add_column("Available Seats", justify="center", style="blue", no_wrap=True)
# table.add_column("Date", justify="center", style="green", no_wrap=True)

# req = re.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict", headers=headers, params=jam)
# req = req.json()

# def find_active(block, is_jam=True, age=18):
#       if is_jam:
#             block_name = "Jamnagar"
#       else:
#             block_name = "Jamnagar Corporation"

#       sessions = block['sessions']

#       for sess in sessions:
#             if sess["min_age_limit"] == age and sess["available_capacity"] > 0:
#                   table.add_row(block["name"], str(sess["available_capacity"]), str(sess["date"]))
#                   # print(block["name"], " -- ", sess["available_capacity"], " -- ", sess["date"])

# for block in req["centers"]:
#       find_active(block, age=18,is_jam=True)
