from django.shortcuts import render
import requests

# Create your views here.

def default_map (request):
    mapbox_access = 'pk.eyJ1IjoidmlyZW5kcmFrYWJyYSIsImEiOiJja3R5NnI3dzEwbmxtMm5xaGZkOTU5d2ppIn0.JhMUOuV4wjTLTerRlvQQWw'

    # i = 0
    # for e in latLng:
    #     if e != "_":
    #         i += 1
    #     else:
    #         break
    # lat = str(latLng[:i])
    # lng = str(latLng[i+1:])

    # print (lat)
    # print (lng)

    lat = request.GET.get('lat')

    lngFloat = float(request.GET.get('lng'))
    lngFloat = ((lngFloat+180)%360)-180         # error handling (mapbox shows even 1000 longitude!!)
    lng = str(lngFloat)

    # print ("--------------------latLng", lat, lng)

    weather_response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lng+'&exclude=minutely,hourly,daily&units=metric&appid=0a666fe2e0184668f89ab03d05280f71').json()

    # print ('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lng+'&exclude=minutely,hourly,daily&units=metric&appid=0a666fe2e0184668f89ab03d05280f71')

    temp = weather_response['current']['temp']                                  # float
    tempFeels = weather_response['current']['feels_like']                       # float
    pressure = weather_response['current']['pressure']
    humidity = weather_response['current']['humidity']
    visibility = weather_response['current']['visibility']
    speed = weather_response['current']['wind_speed']
    main = weather_response['current']['weather'][0]['main']                    # string
    description = weather_response['current']['weather'][0]['description']      # string
    icon = weather_response['current']['weather'][0]['icon']                    # string
    iconURL = "http://openweathermap.org/img/wn/"+icon+"@2x.png"

    context = { 'mapbox_access_token' : mapbox_access, 'lat':lat, 'lng':lng, 'temp':temp, 'tempFeels':tempFeels, 'main':main, 'description':description, 'iconURL':iconURL, 'pressure':pressure, 'humidity':humidity, 'visibility':visibility, 'speed':speed, 'currLat':request.GET.get('currLat'), 'currLng':request.GET.get('currLng'), 'zoom':request.GET.get('zoom'), 'show1':request.GET.get('show')}

    return render(request, 'map.html', context)