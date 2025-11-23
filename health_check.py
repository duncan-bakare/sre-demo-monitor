import requests
from datetime import datetime

# URL of your Flask web service
url = "http://127.0.0.1:5000"

# Open a log file in append mode
with open("monitor.log", "a") as f:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            f.write(f"{datetime.now()} - Service is UP\n")
        else:
            f.write(f"{datetime.now()} - Service returned {r.status_code}\n")
    except Exception as e:
        f.write(f"{datetime.now()} - Service DOWN: {e}\n")
