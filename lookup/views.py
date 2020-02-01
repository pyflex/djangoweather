# this is my views.py file
from django.shortcuts import render

def index(request):
    import json
    import requests

    if request.method == "POST":
        # do this stuff
        zipcode = request.POST["zipcode"]

        api_request = requests.get(
            f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=3272C366-9A19-4A0D-9071-3638FDA1D5AA")

        try:
            api = json.loads(api_request.content)
            quality = api[0]["Category"]["Name"]
            # quality = "Moderate"
            if quality == "Good":
                text = "0 to 50. Air quality is considered satisfactory, and air pollution poses little or no risk."
                class_name = "good"
            elif quality == "Moderate":
                text = "51 to 100. Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                class_name = "moderate"
            elif quality == "Unhealthy for Sensitive Groups":
                text = "101 to 150. Members of sensitive groups may experience health effects. The general public is not likely to be affected."
                class_name = "usg"
            elif quality == "Unhealthy":
                text = "151 to 200. Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                class_name = "unhealthy"
            elif quality == "Very Unhealthy":
                text = "201-250. Health alert: everyone may experience more serious health effects."
                class_name = "very-unhealthy"
            else:
                text = "251 to 300. Health warnings of emergency conditions. The entire population is more likely to be affected."
                class_name = "hazardarous"

        except Exception as e:
            api = "Error..."
            return render(request, "index.html", {"api": api})

        return render(request, "index.html", {"api": api, "text": text, "class_name": class_name})

    else:

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20050&distance=5&API_KEY=3272C366-9A19-4A0D-9071-3638FDA1D5AA")
        
        try:
            api = json.loads(api_request.content)
            quality = api[0]["Category"]["Name"]
            # quality = "Moderate"
            if quality == "Good":
                text = "0 to 50. Air quality is considered satisfactory, and air pollution poses little or no risk."
                class_name = "good"
            elif quality == "Moderate":
                text = "51 to 100. Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                class_name = "moderate"
            elif quality == "Unhealthy for Sensitive Groups":
                text = "101 to 150. Members of sensitive groups may experience health effects. The general public is not likely to be affected."
                class_name = "usg"
            elif quality == "Unhealthy":
                text = "151 to 200. Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                class_name = "unhealthy"
            elif quality == "Very Unhealthy":
                text = "201-250. Health alert: everyone may experience more serious health effects."
                class_name = "very-unhealthy"
            else:
                text = "251 to 300. Health warnings of emergency conditions. The entire population is more likely to be affected."
                class_name = "hazardarous"

        except Exception as e:
            api = "Error..."
            return render(request, "index.html", {"api": api})

        return render(request, "index.html", {"api": api, "text": text, "class_name": class_name})
   
    


def about(request):
    return render(request, 'about.html', {})
