import requests
import tkinter as tk
from bs4 import BeautifulSoup



def get_weather_info():
    location = location_entry.get()
    search = "weather in " + location
    url = f"https://www.google.com/search?&q={search}&hl=en"

    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    condition = s.find("div", class_="BNeawe tAd8D AP7Wnd")
    temperature = s.find("div", class_="BNeawe iBp4i AP7Wnd")

    if condition is not None and temperature is not None:
        condition = condition.text
        temperature = temperature.text
        result_label.config(text=f"Temperature in {location}: {temperature}\nMore Information About {location}: {condition}")
    else:
         result_label.config(text="Invalid location, please enter again.")



#Enter Event
def on_enter(event):
    get_weather_info()


#Window
window = tk.Tk()
window.title("Weather App")
window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)
window.iconbitmap("weather.ico")



#Location Label
location_label = tk.Label(window, text="Enter Location: ")
location_label.pack()

#Location Entry
location_entry = tk.Entry(window)
location_entry.pack()

#Bin Enter And Get Weather
location_entry.bind("<Return>", on_enter)


#BUTTON
get_weather_button = tk.Button(window, text="Get Weather", command =get_weather_info)
get_weather_button.pack()


#Display Weather Label
result_label = tk.Label(window, text="")
result_label.pack()











window.mainloop()