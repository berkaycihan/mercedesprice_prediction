from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Canvas
from tkinter import ttk
from PIL import ImageTk,Image

from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from sklearn import model_selection
import xgboost as xgb
from xgboost import XGBRegressor
import time

df=pd.read_csv('merc_label.csv')
df_2=df.copy()

X = df.drop(["price_tl"], axis = 1)
Y = df["price_tl"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 144)

xgb1 = XGBRegressor(colsample_bytree = 0.5, learning_rate = 0.02, max_depth = 3, n_estimators = 2000)

model_xgb = xgb1.fit(X_train, Y_train)


window = Tk()
window.title(" Interface ")

#BASIC INTERFACE

window.geometry("1700x900")
window.resizable(False, False)

#win.attributes('-fullscreen', False)


background_image=PhotoImage(file="merc_background11-new.gif")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


title_label = Label(window, text = "Prediction of Mercedes Price in Turkey Market with ML", font="helvetica 50",borderwidth=1, padx = 5, pady = 1,
                    background='black',foreground='white')        
title_label.place(x = 50 ,y = 30)

screen1 = Label(window, text= "Loading...",font=("arial italic", 18,'bold'),borderwidth=6,background='black',foreground='white', padx = 72, pady = 40)
screen1.place(x = 720, y = 230)

#ENTRY FUNCTIONS

def message_():
    messagebox.showinfo(title="Successful", message="The process has been successfully selected")

def error_():
    messagebox.showwarning(title="Caution", message="invalid value")


def edit_km():
    global km_
    try:
        km = int(km_entry.get())
        if(999999>km > 0):
            km_ = km
            message_()
            message_km()
        else:
            error_()
    except:
        error_()
        
def edit_age():
    global age_
    try:
        age = int(age_entry.get())
        if(70> age > 0):
            age_ = age
            message_()
            message_age()
        else:
            error_()
    except:
        error_()
    
def fuel_type():
    global fuel
    fuel_type = fuel_box.get()
    if(fuel_type == "Diesel"):
        fuel = 0
        message_()
        message_fuel()
    elif(fuel_type == "Petrol"):
        fuel = 1
        message_()
        message_fuel()
    else:
        error_()
        
def gear_type():
    global gear
    gear_type = gear_box.get()
    if(gear_type == "Automatic"):
        gear = 2
        message_()
        message_gear()
    elif(gear_type == "Semi-Automatic"):
        gear = 1
        message_()
        message_gear()
    elif(gear_type =="Manual"):
        gear = 0
        message_()
        message_gear()
    else:
        error_()
        
def city_turkey():
    global city
    city_type = city_box.get()
    if(city_type == "Istanbul"):
        city = 1
        message_()
        message_city()
    elif(city_type == "Other"):
        city = 0
        message_()
        message_city()
    else:
        error_()
    
def variant_type():
    global variant
    variant_type = variant_box.get()
    if(variant_type == "A 180"):
        variant = 0
        message_()
        message_variant()
    elif(variant_type == "A 200"):
        variant = 12
        message_()
        message_variant()
    elif(variant_type =="B 180"):
        variant = 1
        message_()
        message_variant()
    elif(variant_type =="C 180"):
        variant = 2
        message_()
        message_variant()
    elif(variant_type =="C 200"):
        variant = 4
        message_()
        message_variant()
    elif(variant_type =="C 220"):
        variant = 3
        message_()
        message_variant()
    elif(variant_type =="E 180"):
        variant = 5
        message_()
        message_variant()
    elif(variant_type =="E 200"):
        variant = 6
        message_()
        message_variant()
    elif(variant_type =="E 220"):
        variant = 7
        message_()
        message_variant()
    elif(variant_type =="E 250"):
        variant = 8
        message_()
        message_variant()
    elif(variant_type =="E 300"):
        variant = 10
        message_()
        message_variant()
    elif(variant_type =="E 350"):
        variant = 9
        message_()
        message_variant()
    elif(variant_type =="Other"):
        variant = 11
        message_()
        message_variant()
    else:
        error_()    

def class_type():
    global class_
    class_type = class_box.get()
    if(class_type == "A-Class"):
        class_ = 0
        message_()
        message_class()
    elif(class_type == "B-Class"):
        class_ = 1
        message_()
        message_class()
    elif(class_type =="C-Class"):
        class_ = 2
        message_()
        message_class()
    elif(class_type =="E-Class"):
        class_ = 3
        message_()
        message_class()
    else:
        error_()
        
def engine_type():
    global engine
    engine_type = engine_box.get()
    if(engine_type == "1300 cc and lower"):
        engine = 1
        message_()
        message_engine()
    elif(engine_type == "1301-1600 cc"):
        engine = 0
        message_()
        message_engine()
    elif(engine_type == "1601-1800 cc"):
        engine = 2
        message_()
        message_engine()
    elif(engine_type == "1801-2000 cc"):
        engine = 4
        message_()
        message_engine()
    elif(engine_type == "2001-2500 cc"):
        engine = 3
        message_()
        message_engine()
    elif(engine_type == "2501-3000 cc"):
        engine = 5
        message_()
        message_engine()
    elif(engine_type == "3001-3500 cc"):
        engine = 6
        message_()
        message_engine()
    else:
        error_()
        
#GREEN LIGHT FUNCTIONS
def message_class():
    class_button = Button(window, text = "Save", command = class_type, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    class_button.place(x = 1165, y = 450)
def message_variant():
    variant_button = Button(window, text = "Save", command = variant_type, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    variant_button.place(x = 1165, y = 600)
def message_km():
    km_buton = Button(window, text = "Save", command = edit_km, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    km_buton.place(x = 365, y = 300)
def message_engine():
    engine_button = Button(window, text = "Save", command = engine_type, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    engine_button.place(x = 795, y = 590)
def message_fuel():
    fuel_button = Button(window, text = "Save", command = fuel_type, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    fuel_button.place(x = 365, y = 720)
def message_gear():
    gear_button = Button(window, text = "Save", command = gear_type, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    gear_button.place(x = 795, y = 700)
def message_city():
    city_button = Button(window, text = "Save", command = city_turkey, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    city_button.place(x = 795, y = 170)
def message_age():
    age_buton = Button(window, text = "Save", command = edit_age, font="helvetica 12",background='green',foreground='white',borderwidth=6,width=12,height=1)
    age_buton.place(x = 1165, y = 720)


        
# LABELS
        
#CAR_CLASS

class_label = Label(window, text = "CLASS", font="helvetica 12",borderwidth=6,width=12,height=1)
class_label.place(x = 1165, y = 400)

classes = ['A-Class', 'B-Class', 'C-Class', 'E-Class']
class_box = Combobox(window, values = classes)
class_box.place(x = 1165, y = 430)

class_button = Button(window, text = "Save", command = class_type, font="helvetica 12",borderwidth=6,width=12,height=1)
class_button.place(x = 1165, y = 450)



#VARIANT

variant_label = Label(window, text = "VARIANT", font="helvetica 12",borderwidth=6,width=12,height=1)
variant_label.place(x = 1165, y = 550)

variants = ['A 180', 'A 200', 'B 180', 'C 180', 'C 200', 'C 220',
       'E 180', 'E 200', 'E 220', 'E 250', 'E 300', 'E 350', 'Other']
variant_box = Combobox(window, values = variants)
variant_box.place(x = 1165, y = 580)

variant_button = Button(window, text = "Save", command = variant_type, font="helvetica 12",borderwidth=6,width=12,height=1)
variant_button.place(x = 1165, y = 600)




#KM

km_label = Label(text = "KM", font="helvetica 12",borderwidth=6,width=12,height=1,background='white',foreground='black')
km_label.place(x = 365, y = 250)

km_entry = Entry()
km_entry.place(x = 365, y = 280)

km_buton = Button(window, text = "Save", command = edit_km, font="helvetica 12",borderwidth=6,width=12,height=1)
km_buton.place(x = 365, y = 300)



#ENGINE_CAPACITYCC

engine_label = Label(window, text = "ENGINE CAPACITY(CC)", font="helvetica 12",borderwidth=6,width=20,height=1)
engine_label.place(x = 765, y = 540)

engines = [ '1300 cc and lower','1301-1600 cc', '1601-1800 cc',
        '1801-2000 cc','2001-2500 cc', '2501-3000 cc', '3001-3500 cc']
engine_box = Combobox(window, values = engines)
engine_box.place(x = 795, y = 570)

engine_button = Button(window, text = "Save", command = engine_type, font="helvetica 12",borderwidth=6,width=12,height=1)
engine_button.place(x = 795, y = 590)



#FUEL

fuel_label = Label(window, text = "FUEL TYPE", font="helvetica 12",borderwidth=6,width=12,height=1)
fuel_label.place(x = 365, y = 670)

fuels = ["Diesel","Petrol"]
fuel_box = Combobox(window, values = fuels)
fuel_box.place(x = 365, y = 700)

fuel_button = Button(window, text = "Save", command = fuel_type, font="helvetica 12",borderwidth=6,width=12,height=1)
fuel_button.place(x = 365, y = 720)



#GEAR

gear_label = Label(window, text = "GEAR TYPE", font="helvetica 12",borderwidth=6,width=12,height=1)
gear_label.place(x = 795, y = 650)

gears = ["Automatic","Semi-Automatic","Manual"]
gear_box = Combobox(window, values = gears)
gear_box.place(x = 795, y = 680)

gear_button = Button(window, text = "Save", command = gear_type, font="helvetica 12",borderwidth=6,width=12,height=1)
gear_button.place(x = 795, y = 700)



#CITY

city_label = Label(window, text = "CITY IN TURKEY", font="helvetica 12",borderwidth=6,width=12,height=1)
city_label.place(x = 795, y = 120)

cities = ["Istanbul","Other"]
city_box = Combobox(window, values = cities)
city_box.place(x = 795, y = 150)

city_button = Button(window, text = "Save", command = city_turkey, font="helvetica 12",borderwidth=6,width=12,height=1)
city_button.place(x = 795, y = 170)



#AGE

age_label = Label(text = "AGE", font="helvetica 12",borderwidth=6,width=12,height=1,background='white',foreground='black')
age_label.place(x = 1165, y = 670)

age_entry = Entry()
age_entry.place(x = 1165, y = 700)

age_buton = Button(window, text = "Save", command = edit_age, font="helvetica 12",borderwidth=6,width=12,height=1)
age_buton.place(x = 1165, y = 720)



#MACHINE LEARNING 



def calculate():
    
    time.sleep(1)

    new_data = [[class_],[variant],[km_],[engine],[fuel],[gear],[city],[age_]]  
    new_data = pd.DataFrame(new_data).T

    df_2 = new_data.rename(columns = {0:"class_",
                        1:"variant_",
                        2:"km",
                        3:"engine_capacity_cc",
                        4:"fuel",
                        5:"gear",
                        6:"city",
                        7:"age"})
    
    pred = model_xgb.predict(df_2)
    
    if(pred < 0):
        pred = -1*pred
    if(pred>2000000):
        pred=0
    
    pred = int(pred)
    
    screen2 = Label(window, text = str(pred)+ " ₺",font=("arial italic", 18,'bold'),borderwidth=6,background='black',foreground='green', padx = 72, pady = 40)
    screen2.place(x = 720, y = 225)
    

#CALCULATE BUTTON

calculate_button = Button(window, text = "Calculate", command = calculate,background='red',borderwidth=6,width=8,height=3,font="Verdana 26 bold")
calculate_button.place(x = 745, y = 360)


#MORE

def more():
    T = Text(window, height=14, width=55,padx=20, pady=20,borderwidth=6,background='#fffdd0')
    T.place(x=1165, y=110)
    quote = """#1024 used Mercedes vehicles data was scraped from the car gallery website, then edited and the regression model was built.
#XGBoost algorithm was used.
Test score: 0.9558197675181905
MSE value: 71178.69893701086
The exchange rate in the date it was done:
1 EURO = 9.2902 TURKISH LIRAS 23/03/2021

Contact:
github.com/berkaycihan
kaggle.com/berkaycihan
linkedin.com/in/berkaycihan
thanks @keyiflerolsun KekikAkademi
"""
    T.insert(END, quote)
    opened=0
    

more_label = Label(text = "SHOW MORE", font="helvetica 12",borderwidth=6,width=17,height=1,background='blue',foreground='white')
more_label.place(x = 1351, y = 520)


more_image=PhotoImage(file="darwin_mini2.png")

more_button1 = Button(window, text = "More Info", command = more, image=more_image,borderwidth=6,width=153,height=213,bg='black')

more_button1.place(x=1351, y=551)






mainloop()
