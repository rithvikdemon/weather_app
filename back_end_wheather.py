import requests
import json
import datetime


def gettemp(cit):

    weather_dict={}

    
    c=cit
    url1 = ('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=0ff996d0a48a1949adcbced2f6efa5f9&units=metric'%c)
    res1 = requests.get(url1)
    data1 = res1.json()
    
    weather_dict["T"] = data1['main']['temp']
    weather_dict["H"] = data1['main']['humidity']
    weather_dict["P"] = data1['main']['pressure']
    weather_dict["WS"] = data1['wind']['speed']
    weather_dict["WD"] = data1['wind']['deg']
    weather_dict["WDS"] = data1['weather'][0]['description']
    weather_dict["NA"]=data1['name']

    return weather_dict
        

def getforecast(cityna):
    
    c=cityna
    url2 = ('http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=0ff996d0a48a1949adcbced2f6efa5f9&units=metric'%c)
    res2 = requests.get(url2)
    data2 = res2.json()

    d=datetime.datetime.now() + datetime.timedelta(days=1)
    d1 = d.strftime("%Y-%m-%d 12:00:00")

    d=datetime.datetime.now() + datetime.timedelta(days=2)
    d2 = d.strftime("%Y-%m-%d 12:00:00")

    d=datetime.datetime.now() + datetime.timedelta(days=3)
    d3 = d.strftime("%Y-%m-%d 12:00:00")

    forecast_dict={}

    l_data = len(data2['list'])

    for i in range(l_data):
        if d1 == data2['list'][i]['dt_txt']:
            forecast_dict["T1"]=data2['list'][i]['main']['temp']
            forecast_dict["H1"]=data2['list'][i]['main']['humidity']
            forecast_dict["P1"]=data2['list'][i]['main']['pressure']
            forecast_dict["Des1"]=data2['list'][i]['weather'][0]['description']       
            #print(f_dict1["T"],f_dict1["H"],f_dict1["Des"])

    for i in range(l_data):
        if d2 == data2['list'][i]['dt_txt']:
            forecast_dict["T2"]=data2['list'][i]['main']['temp']
            forecast_dict["H2"]=data2['list'][i]['main']['humidity']
            forecast_dict["P2"]=data2['list'][i]['main']['pressure']
            forecast_dict["Des2"]=data2['list'][i]['weather'][0]['description']       
            #print(f_dict2["T"],f_dict2["H"],f_dict2["Des"])
            
    for i in range(l_data):
        if d3 == data2['list'][i]['dt_txt']:
            forecast_dict["T3"]=data2['list'][i]['main']['temp']
            forecast_dict["H3"]=data2['list'][i]['main']['humidity']
            forecast_dict["P3"]=data2['list'][i]['main']['pressure']
            forecast_dict["Des3"]=data2['list'][i]['weather'][0]['description']       
            #print(f_dict3["T"],f_dict3["H"],f_dict3["Des"])

    return forecast_dict
