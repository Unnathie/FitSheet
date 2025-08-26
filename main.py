import os
from datetime import datetime
import requests
API_ID=os.getenv("ID")
API_KEY=os.getenv("KEY")
headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}
urlc="https://trackapi.nutritionix.com"
sheety_url=os.getenv("SHEET_ENDPOINT")
exercise_endpoint="/v2/natural/exercise"
exercise={
    "query":input("how many hours of exercise did you do? ")
}
res=requests.post(url=f"{urlc}{exercise_endpoint}",headers=headers,json=exercise)
response=res.json()
date_time=str(datetime.now()).split(" ")
sheets_in = {
    "workout": {
        "date": date_time[0],
        "time": date_time[1][:8],
        "exercise": response["exercises"][0]["user_input"],
        "duration": response["exercises"][0]["duration_min"],
        "calories": response["exercises"][0]["nf_calories"]
    }
}
sheet_response = requests.post(
  sheety_url,
  json=sheets_in,
  auth=(
      os.getenv("USER_NAME"),
      os.getenv("PASSWORD"),
  )
)
print(sheet_response.text)