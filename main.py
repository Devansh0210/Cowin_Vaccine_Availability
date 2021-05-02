import requests as re
import json
import time
from datetime import date
from rich.console import Console
from rich.table import Table
from find_act import *
from plyer import notification
import fire

console = Console()

def notify_me():
      
      notification.notify(
            title='Vaccine Available',
            message='Go !! Grab the Vaccine !!!!',
            app_icon=None,
            timeout=10,  
      )

def start(age):

      while True:
            time.sleep(2)
            data = get_data(centers, age=age)
            if len(data) > 0:
                  notify_me()
                  console.print(get_data(centers, age=age, req_table=True))
                  break

if __name__ == '__main__':
      fire.Fire(start)

# print(req.json())
# print(json.dumps(req, indent=4, sort_keys=True))