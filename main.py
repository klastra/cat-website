from flask import Flask, render_template
from datetime import date
import requests
import json

today = date.today()
print(today)
today = today.strftime("%B %d, %Y")

weather_list = []
sunnyvale = requests.get("http://api.openweathermap.org/data/2.5/weather?q=sunnyvale,usa&APPID=d8a60d888e21ca044f09ecdef0bccb5a")

sunnyvalejson =  sunnyvale.json()

svweather = (sunnyvalejson['weather'])
svweather = str(svweather).split(",")
weather_description = svweather[2].split(":")
weather_description = weather_description[1].strip("'").upper()

def convertToFahrenheit(kelvin):
    fahrenheit = kelvin - 273.25
    fahrenheit = fahrenheit * 1.8
    fahrenheit = fahrenheit + 32
    return round(fahrenheit)

svmain = sunnyvalejson["main"]

svmain = str(svmain).split(",")
temp1 = svmain[0].split(":")
temp_min = svmain[2].split(":")
temp_max = svmain[3].split(":")
humidity = svmain[5].split(":")
humidity = humidity[1].strip("}")


temp1_convertF = convertToFahrenheit(float(temp1[1]))
temp_min_convert = convertToFahrenheit(float(temp_min[1]))
temp_max_convert = convertToFahrenheit(float(temp_max[1]))


#FLASK
app = Flask(__name__)

@app.route("/")


def home():
    return render_template("index.html", friends = ["Kirsty", "Noel", "Gloria", "Ryan", "Oreo"], date = today, weather = weather_description, temp = temp1_convertF,
                           temp_high = temp_max_convert, temp_low = temp_min_convert, hum = humidity)

if __name__ == "__main__":
    app.run(debug = True, port = 2021)


