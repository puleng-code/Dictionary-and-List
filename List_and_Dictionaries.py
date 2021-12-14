# Data

weather_dict = {"city": "Cape Town", "weather":[{"id":802,"main":"Clouds","description":"scattered clouds"}, {"id": 900}], "main": {"temp":290.85,"feels_like":290.74}, "wind": {"speed": [1.79, 2.22]}}
print(weather_dict)
print("\n")
print(weather_dict["city"])
print(weather_dict["main"]["temp"])
print(weather_dict["weather"][0]["description"])
print(weather_dict["weather"][1]["id"])
print(weather_dict["wind"]["speed"][1])