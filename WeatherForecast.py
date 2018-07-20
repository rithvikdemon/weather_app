from tkinter import *
from PIL import Image, ImageTk
from back_end_wheather import getforecast, gettemp
import datetime

#printing about menu
def About():
    top2 = Toplevel()
    top2.title("Weather Forecast")
    top2.geometry('400x300')
    top2.config(bg="SteelBlue2")

    info = Label(top2,text=" Owner: Rithvik\n\nContact: example@gmail.com")
    info.place(relx=0.5,rely=0.5,anchor=CENTER)
    info.config(bg="SteelBlue2",fg="black",font=("Courier 12 bold"))

    B3= Button(top2,text='EXIT',command=top2.destroy)
    B3.config(bg="white",fg="Steelblue2")
    B3.place(relx=0.5,rely=0.95,anchor=S)



# printing Weather forecast for next 3 days
def Forecast_Window():
    fw = {}
    cit=cityinput.get()
    fw = getforecast(cit)
    
    
    top = Toplevel()
    top.title("Weather Forecast")
    top.geometry('700x425')
    top.config(bg="wheat3")

    city = Label(top,text=cit.upper())
    city.place(relx=0.07,rely=0.13,anchor=NW)
    city.config(bg="wheat3",fg="SteelBlue2",font=("Courier 17 bold"))


    d=datetime.datetime.now() + datetime.timedelta(days=1)
    d1 = d.strftime("%d-%b-%Y")

    d=datetime.datetime.now() + datetime.timedelta(days=2)
    d2 = d.strftime("%d-%b-%Y")

    d=datetime.datetime.now() + datetime.timedelta(days=3)
    d3 = d.strftime("%d-%b-%Y")

    date1 = Label(top,text=d1)
    date1.config(bg="White",font=("Courier", 9))
    date1.place(relx=0.40,rely=0.15,anchor=N)

    date2 = Label(top,text=d2)
    date2.config(bg="White",font=("Courier", 9))
    date2.place(relx=0.60,rely=0.15,anchor=N)

    date3 = Label(top,text=d3)
    date3.config(bg="White",font=("Courier", 9))
    date3.place(relx=0.80,rely=0.15,anchor=N)

    
    head = Label(top,text='WEATHER')
    head.config(bg="White",font=("Courier", 18))
    head.place(relx=0.5,rely=0,anchor=N)

    tem = Label(top,text="Temperature :")
    tem.config(bg="ghost white",fg="black",font=("Courier 11"))
    tem.place(relx=0.04,rely=0.30,anchor=W)

    humi = Label(top,text="Humidity :")
    humi.config(bg="ghost white",fg="black",font=("Courier 11 "))
    humi.place(relx=0.04,rely=0.45,anchor=W)

    pres = Label(top,text="Pressure :")
    pres.config(bg="ghost white",fg="black",font=("Courier 11 "))
    pres.place(relx=0.04,rely=0.60,anchor=W)

    desc = Label(top,text="Description :")
    desc.config(bg="ghost white",fg="black",font=("Courier 11 "))
    desc.place(relx=0.04,rely=0.75,anchor=W)

    #printing temperature
    tem1 = Label(top,text="%d'C"%fw['T1'])
    tem1.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem1.place(relx=0.37,rely=0.30,anchor=W)

    tem2 = Label(top,text="%d'C"%fw['T2'])
    tem2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem2.place(relx=0.57,rely=0.30,anchor=W)

    tem3 = Label(top,text="%d'C"%fw['T3'])
    tem3.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem3.place(relx=0.77,rely=0.30,anchor=W)

    #printing humidity
    hum1 = Label(top,text="{}%".format(fw['H1']))
    hum1.config(bg="wheat3",fg="black",font=("Courier 12 "))
    hum1.place(relx=0.37,rely=0.45,anchor=W)

    hum2 = Label(top,text="{}%".format(fw['H2']))
    hum2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    hum2.place(relx=0.57,rely=0.45,anchor=W)

    hum3 = Label(top,text="{}%".format(fw['H3']))
    hum3.config(bg="wheat3",fg="black",font=("Courier 12 "))
    hum3.place(relx=0.77,rely=0.45,anchor=W)

    #printing pressure
    pres1 = Label(top,text="%d hPa"%fw['P1'])
    pres1.config(bg="wheat3",fg="black",font=("Courier 12 "))
    pres1.place(relx=0.37,rely=0.60,anchor=W)

    pres2 = Label(top,text="%d hPa"%fw['P2'])
    pres2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    pres2.place(relx=0.57,rely=0.60,anchor=W)

    pres3 = Label(top,text="%d hPa"%fw['P3'])
    pres3.config(bg="wheat3",fg="black",font=("Courier 12 "))
    pres3.place(relx=0.77,rely=0.60,anchor=W)

    #printing description
    tem2 = Label(top,text="%s"%fw['Des1'])
    tem2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem2.place(relx=0.30,rely=0.75,anchor=W)

    tem2 = Label(top,text="%s"%fw['Des2'])
    tem2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem2.place(relx=0.50,rely=0.75,anchor=W)

    tem2 = Label(top,text="%s"%fw['Des3'])
    tem2.config(bg="wheat3",fg="black",font=("Courier 12 "))
    tem2.place(relx=0.76,rely=0.75,anchor=W)

    B3= Button(top,text='  EXIT  ',command=top.destroy)
    B3.config(bg="white",fg="black")
    B3.place(relx=0.5,rely=0.95,anchor=S)

    top.mainloop()


def future_forecast():
    forecast = Label(root,text="3-Days Forecast")
    forecast.config(bg="white",fg="SteelBlue4",font="Courier 12")
    forecast.place(relx=0.8,rely=0.13,anchor=N)

    B2= Button(root,text='Show Forecast',command=Forecast_Window)
    B2.config(bg="white",fg="black")
    B2.place(relx=0.8,rely=0.25,anchor=N)


#calling Backenweather function
def backendcall():
    s=cityinput.get()
    forecast={}
    forecast = gettemp(s)
    showtemp(forecast)

#printing Current weather forecast
def showtemp(wf):

    cityna = Label(root,text=wf['NA'])
    cityna.place(relx=0.5,rely=0.4,anchor=CENTER)
    cityna.config(bg="white",fg="SteelBlue4",font=("Courier 17 bold"))

    date = Label(root,text=datetime.datetime.now().strftime("%d %b %Y"))
    date.place(relx=0.5,rely=0.5,anchor=CENTER)
    date.config(bg="white",fg="SteelBlue4",font=("Courier 13 bold"))
    
    temp = Label(root,text="Temperature: %s°C"%wf['T'])
    temp.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    temp.place(relx=0.03,rely=0.7,anchor=W)

    humi = Label(root,text="Humidity : {}%".format(wf['H']))
    humi.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    humi.place(relx=0.78,rely=0.7,anchor=W)

    pres = Label(root,text="Pressure : %d hPa"%wf['P'])
    pres.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    pres.place(relx=0.73,rely=0.8,anchor=W)

    wsp = Label(root,text="Wind Speed : %d m/s"%wf['WS'])
    wsp.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    wsp.place(relx=0.15,rely=0.8,anchor=CENTER)
   
    wdr = Label(root,text="Wind Direction : %d'"%wf['WD'])
    wdr.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    wdr.place(relx=0.7,rely=0.9,anchor=W)

    wds = Label(root,text="Weather Description : %s"%wf['WDS'])
    wds.config(bg="cadetblue1",fg="black",font=("Courier 12 bold"))
    wds.place(relx=0.03,rely=0.9,anchor=W)

    future_forecast()
   
#Main
root = Tk()
root.geometry('750x425')

image = Image.open('weather.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image = photo_image)

root.title('Weather')

head = Label(root,text='WEATHER')
head.config(bg="white",fg="SteelBlue4",font=("Courier 22 "))
head.place(relx=0.5,rely=0,anchor=N)

city = Label(root,text='ENTER CITY:',font="Courier 9 ")
city.config(bg="white",fg="SteelBlue4")
city.place(relx=0.03,rely=0.13,anchor=NW)

cityinput = Entry(root)
cityinput.place(relx=0.14,rely=0.13,anchor=NW)

B1= Button(root,text='Show Weather',command=backendcall)
B1.config(bg="white",fg="black")
B1.place(relx=0.16,rely=0.20,anchor=NW)

menu = Menu(root)
root.config(menu=menu)
filemenu= Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='EXIT',command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)



label.grid(row=0,column=0)
root.mainloop()
