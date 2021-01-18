import requests
import datetime
data = datetime.datetime.now()
headers = {
    "x-app-id": "4f6e0d73",
    "x-app-key": "f6e070ce8bcfe5efc534af74598692f6"
}
parameters = {
    "query": str(input()),
    "gender": "male",
    "weight_kg": 52.0,
    "height_cm": 168.0,
    "age": 19
}

req = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=parameters).json()

authentication = {
    "Authorization": "Bearer ajh3uthaslf3hsdgkj"
}

for exercise in req["exercises"]:
    adding = {
        "workout": {
            "date": data.strftime("%d/%m/%Y"),
            "time": data.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    smreq = requests.post("https://api.sheety.co/f75d7751c616d5c4ab009c376dc89542/workout/workouts", json=adding, headers=authentication)

    print(smreq.json())

