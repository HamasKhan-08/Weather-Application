# Importing all the required modules for the application to functions properly and as intended
from tkinter import *
import tkinter as tk
from geopy.geocoders import  Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import  requests
import pytz

root=Tk()
root.title("Weather 24/7") # Title of the application
root.geometry("900x500+300+200") # Setting an appropriate canvas size for the weather application

def getweather():

    city = textfield.get() # Assigning the variable "city" to the text entered by the user in the search box
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    Zone = TimezoneFinder() # Looking up the corresponding timezone, assigning a variable to it
    result = Zone.timezone_at(lng=location.longitude,lat=location.latitude) # Findout out the time using city
    
    Home = pytz.timezone(result)
    Loc_Time = datetime.now(Home)
    Curr_Time = Loc_Time.strftime("%I:%M %p")
    name.config(text = Curr_Time)

    # Weather API and Data Functions, Calling The API
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=58bf452b6c86cc517caab41c054bdd05"
    Json = requests.get(api).json() # Using requests module to send requests to the API to get all the data
    condition = Json['weather'][0]['main'] # Getting the condition data
    description = Json['weather'][0]['description'] # Getting the description data 
    temp = int((Json['main']['temp']-272.15)) # Getting data of the temperature
    pressure = Json['main']['pressure'] # Getting data of the pressure
    humidity = Json['main']['humidity'] # Getting data of humidity
    wind = Json['wind']['speed'] # Getting data of the wind speed from the API

    # Displaying all the data recieved.

    t.config(text = (temp,"°")) 
    c.config(text = (condition,"|","Feels","Like",temp,"°"))
    w.config(text = (wind,"mph"))
    h.config(text = (humidity,"g/m³"))
    p.config(text = (pressure,"mbar"))
    d.config(text = description)




#  Designing the GUI for the Search Bar, placing an empty bar to act as a place for users to type in.

Search_image=PhotoImage(file="search_bar.png")
myimage=Label(image=Search_image)
myimage.place(x=200,y=20)
textfield=tk.Entry(root,justify="center", width=17,font=("Times",25,"bold"),bg="#404040",border=0,fg="white") # Designing the textfield where the user will enter their city.
textfield.place(x=280,y=40)
textfield.focus()

# Designing the GUI For the search button, placing the search image that will act as a button.

Search_Glassicon=PhotoImage(file="search_glass.png")
myimage_icon=Button(image=Search_Glassicon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=580,y=34)


# Weather image below, it will be accompanied by the results such as the time and the temperature.

Clouds_Image=PhotoImage(file="weather.png")
logo=Label(image=Clouds_Image)
logo.place(x=300,y=100)

# Desinging the container, using an empty container in which the information will be displayed.

Container_Image=PhotoImage(file="bar.png")
container_myimage=Label(image=Container_Image)
container_myimage.pack(padx=6,pady=6,side=BOTTOM)

# GUI For The Local Time Display

name = Label (root,font=("Times",15,"bold"))
name.place (x=150,y=250)
clock = Label (root,font=("Times",20))
clock.place (x=130,y=250)


# Below Are All The Labels Required

Lbl1=Label(root,text="Wind Speed",font=("Times",12,'bold'),fg="white",bg="#ffa38b") # Label for Wind Speed
Lbl1.place(x=110,y=400)

Lbl2=Label(root,text="Humidity",font=("Times",12,'bold'),fg="white",bg="#ffa38b") # Label for Humidity
Lbl2.place(x=280,y=400)

Lbl3=Label(root,text="Overview",font=("Times",12,'bold'),fg="white",bg="#ffa38b") # Label for the Overview
Lbl3.place(x=430,y=400)

Lbl4=Label(root,text="Barometric Pressure",font=("Times",12,'bold'),fg="white",bg="#ffa38b") # Label for the Barometric Pressure
Lbl4.place(x=650,y=400)

t=Label(font=("Times",70,"bold"),fg="#ee666d") # Font Style and Size for the Temperature Display
t.place(x=600,y=150) # Placing the Temperature Display

c=Label(font=("Times",15,'bold')) # Font Style and Size for the Condition
c.place(x=600,y=250) # Placing the Condition Accordingly

w=Label(text="N/A",font=("Times",20,"bold",),bg="#ffa38b") # Font Style and Size For the Default Display...
w.place(x=120,y=430) # Placing the Weather Accordingly

h=Label(text="N/A",font=("Times",20,"bold",),bg="#ffa38b") # Humidity Font Style and Size
h.place(x=280,y=430) # Placing Accordingly


d=Label(text="N/A",font=("Times",20,"bold",),bg="#ffa38b") # Font Style, Size for the Description
d.place(x=430,y=430) # Placement


p=Label(text="N/A",font=("Times",20,"bold",),bg="#ffa38b") # Font Size and Style for Pressure
p.place(x=650,y=430) # Placement for the Pressure Display


root.mainloop() # Displaying the output
